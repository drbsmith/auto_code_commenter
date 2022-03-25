



import sys, os

from util.log import setup_logging
## logger : TODO_DOC
logger = setup_logging()




def main():
	# arg 1 has to be a directory
	path = sys.argv[1]

	if not path[-1] == '/':
		path += '/'

	from sql_databases.connector import ConnectionSettings

	settings = ConnectionSettings()

	settings.user=os.getenv("DBUSER")
	settings.password=os.getenv("DBPASS")
	settings.host='127.0.0.1'
	settings.database="boardable"

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
	if len(sys.argv) < 2:
		logger.error('missing required path to directory argument')
		exit()
		
	try:
		main()
	except:
		logger.error(__file__, exc_info=True)
	finally:
		from sql_databases.connector import CleanUpSSHTunnel
		CleanUpSSHTunnel()