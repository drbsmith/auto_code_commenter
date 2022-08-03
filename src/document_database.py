"""! @file

# Generate Docs for a database

Builds a file structure of .md files that can then be processed using Doxygen.

## Arguments

python3 src/document_database.py root host database user password (port) (schema)

@package src """



import sys, os

from util.log import setup_logging
logger = setup_logging()




def main():
	# arg 1 has to be a directory
	path = sys.argv[1]

	if not path[-1] == '/':
		path += '/'

	from sql_databases.connector import ConnectionSettings

	settings = ConnectionSettings()

	settings.host_name=sys.argv[2]
	settings.database=sys.argv[3]
	settings.user=sys.argv[4]
	settings.password=sys.argv[5]
	if len(sys.argv) > 6:
		settings.port = sys.argv[6]

	from sql_databases.mysql_utils import Mysql

	db = Mysql(settings)
	tables = db.GetTables()

	root = path + settings.database

	if not os.path.exists(root):
		os.makedirs(root)

	# make root / package file:
	if not os.path.exists(root + "/database.md"):
		from sql_databases.make_database_md import MakeRootMarkdown
		root_md = MakeRootMarkdown(settings.database, 'public', tables)

		with open(root + "/database.md", 'w') as f:
			f.write(root_md)

	root += '/tables'
	if not os.path.exists(root):
		os.makedirs(root)

	for t in tables:
		t_path = root + "/{}.md".format(t)
		if not os.path.exists(t_path):
			with open(t_path, 'w') as f:
				pass




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