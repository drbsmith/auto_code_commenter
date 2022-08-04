



import sys, os

from util.log import setup_logging
## logger : TODO_DOC
logger = setup_logging()




def main():
	# arg 1 has to be a directory
	path = sys.argv[1]

	if not path[-1] == '/':
		path += '/'

	FORCE = False
	if '-force' in sys.argv:
		FORCE = True

	from sql_databases.connector import ConnectionSettings

	settings = ConnectionSettings()

	if '-mysql' in sys.argv:
		settings.user=os.getenv("DBUSER")
		settings.password=os.getenv("DBPASS")
		settings.host='127.0.0.1'
		settings.database="boardable"

		from sql_databases.mysql_utils import Mysql

		db = Mysql(settings)
	else:
		settings.host_name=os.environ.get('DATASTORE_DB')
		settings.password=os.environ.get('POSTGRE_P2')
		settings.user='postgres'
		settings.database="postgres"

		from sql_databases.postgres_utils import Postgres

		db = Postgres(settings)

	tables = db.GetTables()

	root = path + settings.database

	if not os.path.exists(root):
		os.makedirs(root)

	# make root / package file:
	if not os.path.exists(root + "/database.md") or FORCE:
		from sql_databases.make_database_md import MakeRootMarkdown
		root_md = MakeRootMarkdown(settings.database, 'public', tables, db.version)

		with open(root + "/database.md", 'w') as f:
			f.write(root_md)

	root += '/tables'
	if not os.path.exists(root):
		os.makedirs(root)

	df = db.GetSchema()

	from sql_databases.make_database_md import MakeTableMarkdown
	for t in tables:
		t_path = root + "/{}.md".format(t)
		if not os.path.exists(t_path) or FORCE:
			table = db.GetOneTable(t) # df.loc[df['TABLE_NAME']==t]

			md = MakeTableMarkdown(settings.database, 'public', t, table)
			with open(t_path, 'w') as f:
				f.write(md)




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