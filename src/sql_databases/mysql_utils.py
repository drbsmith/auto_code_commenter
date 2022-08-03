"""! @file

Note: checks for presence of .env variable SSH_HOST, and if found will create an SSH tunnel to access the db.

@package sql_databases """




import sys, os
p = os.path.dirname(os.path.abspath('./src/sql_databases'))
sys.path.append(p)

from util.log import setup_logging
logger = setup_logging()

from sql_databases.connector import ConnectionSettings, QueryDatabase

class Mysql():
	def __init__(self, settings):
		self.settings = settings
		self.schema = None


	def GetSchema(self):
		if not self.schema is None:
			return self.schema

		# get a mysql database table
		query = """SELECT
				`COLUMN_NAME`
			FROM
				`INFORMATION_SCHEMA`.`COLUMNS`
			WHERE
				TABLE_NAME = 'COLUMNS'
				AND table_schema = 'INFORMATION_SCHEMA'
			ORDER BY
				ordinal_position;"""

		ssh_req = (not os.getenv('SSH_HOST') is None)
		columns = QueryDatabase(query, SETTINGS=self.settings, SSH=ssh_req, MYSQL=True)
	
		data = QueryDatabase("""SELECT
				*
			FROM
				`INFORMATION_SCHEMA`.`COLUMNS` 
			WHERE
				`TABLE_SCHEMA` = '{}';""".format(self.settings.database),
			SETTINGS=self.settings, SSH=ssh_req, MYSQL=True)

		table = []
		for dat in data:
			entry = {}
			for col, d in zip(columns, dat):
				entry[col[0]] = d
			table.append(entry)

		import pandas as pd
		df = pd.DataFrame(table)

		self.schema = df

		return self.schema

	def GetTables(self):
		"""! Get all table names from our schema """
		if self.schema is None:
			self.GetSchema()

		return list(set(self.schema['TABLE_NAME']))


def main():
	settings = ConnectionSettings()

	settings.user=os.getenv("DBUSER")
	settings.password=os.getenv("DBPASS")
	settings.host='127.0.0.1'
	settings.database="boardable"
	# settings.port=prod_tunnel.local_bind_port

	db = Mysql(settings)

	print(db.GetTables())

	return

if __name__ == '__main__':
	try:
		main()
	except:
		pass
	finally:
		# close any open SSH tunnels
		from sql_databases.connector import CleanUpSSHTunnel
		CleanUpSSHTunnel()