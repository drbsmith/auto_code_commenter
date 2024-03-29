




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
		self.version = ''
		self.db_name = ''

		# initialize our data
		self.GetSchema()

	def GetSchema(self):
		if not self.schema is None:
			return self.schema
		ssh_req = (not os.getenv('SSH_HOST') is None)

		self.db_name = self.settings.database

		self.version = QueryDatabase("SELECT VERSION();", SETTINGS=self.settings, SSH=ssh_req, MYSQL=True)
		self.version = self.version[0][0]

		# get a mysql database table
		query = """SELECT
				`COLUMN_NAME`
			FROM
				`INFORMATION_SCHEMA`.`COLUMNS`
			WHERE
				TABLE_NAME = 'COLUMNS'
				AND TABLE_SCHEMA = 'INFORMATION_SCHEMA'
			ORDER BY
				ORDINAL_POSITION;"""

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
		# convert all to lower case
		df.columns = map(str.lower, df.columns)

		self.schema = df

		return self.schema

	def GetTables(self):
		"""! Get all table names from our schema """
		if self.schema is None:
			self.GetSchema()

		return list(set(self.schema['table_name']))

	def GetOneTable(self, table_name):
		return self.schema.loc[self.schema['table_name'] == table_name]

	def MakeNotesTemplate(self):
		"""! Make a file that can have notes manually written in it, which will then be folded into the markdown files.
		"""
		schema = self.schema
		out = {self.db_name: {}}

		tables = self.GetTables()

		t_dict = {}
		for table in tables:
			tdf = self.GetOneTable(table)

			entry = {}
			for idx, row in tdf.iterrows(): ### FINISH THIS! - get a dict with an empty string for each column. {'id': '', 'created': '', 'updated': ''...
				entry[row['column_name']] = ""
			t_dict[table] = entry
		out[self.db_name] = t_dict

		return out
			


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