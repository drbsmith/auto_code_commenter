"""! @file

# Generate Docs for a database

Builds a file structure of .md files that can then be processed using Doxygen.

## Arguments

python3 src/document_database.py root host database user password (port) (schema)

@package src """


##\cond
import sys, os, json

from util.log import setup_logging
logger = setup_logging()
##\endcond



def main():
	# arg 1 has to be a directory
	path = sys.argv[1]

	if not path[-1] == '/':
		path += '/'
	FORCE = False
	if '-force' in sys.argv:
		FORCE = True

	# setup the connection settings. Use args provided by the command executor
	from sql_databases.connector import ConnectionSettings

	settings = ConnectionSettings()

	settings.host_name=sys.argv[2]
	settings.database=sys.argv[3]
	settings.user=sys.argv[4]
	settings.password=sys.argv[5]
	if len(sys.argv) > 6:
		settings.port = sys.argv[6]

	# create a Mysql object, which will pull its own schema right away
	from sql_databases.mysql_utils import Mysql

	db = Mysql(settings)
	tables = db.GetTables()

	## root: the path to the directory we will create the documentation files in
	root = path + settings.database

	if not os.path.exists(root):
		os.makedirs(root)

	# make root / package file:
	if not os.path.exists(root + "/database.md"):
		from sql_databases.make_database_md import MakeRootMarkdown
		root_md = MakeRootMarkdown(settings.database, 'public', tables)

		with open(root + "/database.md", 'w') as f:
			f.write(root_md)

	# check for a notes file, and if not found initiate a blank notes variable
	notes_dict = db.MakeNotesTemplate()
	if os.path.exists(root + "/notes.json"):
		with open(root + "/notes.json", 'r') as f:
			notes_dict = json.load(f)

	# make a tables directory to contain the table files
	table_root = root + '/tables'
	if not os.path.exists(table_root):
		os.makedirs(table_root)

	# go through each table and build a file for each.
	import pandas as pd
	from sql_databases.make_database_md import MakeTableMarkdown

	for t in tables:
		t_path = table_root + "/{}.md".format(t)
		if not os.path.exists(t_path) or FORCE:
			table = db.GetOneTable(t) # df.loc[df['TABLE_NAME']==t]

			n = None
			if t in notes_dict[settings.database]:
				n = notes_dict[settings.database][t]
			else:
				notes_dict[settings.database][t] = {} # need to fill with columns!

			md = MakeTableMarkdown(settings.database, 'public', t, table, NOTES=n)
			with open(t_path, 'w') as f:
				f.write(md)

	with open(root + "/notes.json", 'w') as f:
		json.dump(notes_dict, f)




if __name__ == '__main__':
	if len(sys.argv) < 6:
		logger.error('missing required arguments: root_directory host database user password')
		exit()

	print(sys.argv)
		
	try:
		main()
	except:
		logger.error(__file__, exc_info=True)
	finally:
		from sql_databases.connector import CleanUpSSHTunnel
		CleanUpSSHTunnel()