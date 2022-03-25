

import logging
# connecting assisting functions, wrappers around psycopg

def QueryDatabase(query, SETTINGS=None, SCHEMA=None, SSH=None):
	"""! Query either the 'data lake' postgres db, or the heap-rs3 'data warehouse'. """
	if SSH:
		try:
			prod_tunnel
		except NameError:
			prod_tunnel = CreateSSHTunnel()
			prod_tunnel.start()

		import mysql.connector

		try:
			mydb = mysql.connector.connect(
				user=SETTINGS.user,
				password=SETTINGS.password,
				host='127.0.0.1',
				database=SETTINGS.database,
				port=prod_tunnel.local_bind_port)
			mycursor = mydb.cursor()
			mycursor.execute(query)
			res = mycursor.fetchall()

			mycursor.close()
			mydb.close()
			
			return res
		except mysql.connector.errors.ProgrammingError:
			logging.error(query, exc_info=True)

			exit()
		finally:
			mycursor.close()
			mydb.close()
	else:	
		mydb = _getDBConnector(SETTINGS=SETTINGS, SCHEMA=SCHEMA)
		mycursor = mydb.cursor()

		mycursor.execute(query)
		res = mycursor.fetchall()

		mycursor.close()
		mydb.close()

		return res

def UpdateTable(query, SETTINGS=None):
	"""! Execute a command on the specified database (DATABASE). Does not return any results.
	"""
	if query == '' or query is None:
		return None

	import psycopg2
	try:
		mydb = _getDBConnector(SETTINGS=SETTINGS)
		mycursor = mydb.cursor()

		mycursor.execute(query)
		mydb.commit()

	except (Exception, psycopg2.Error) as error:
		logging.warning("Error in update operation: {}".format(error), exc_info=True)

	finally:
		# closing database connection.
		if (mydb):
			mycursor.close()
			mydb.close()

class ConnectionSettings():
	host_name = ''
	password = ''
	database = ''
	user = ''
	options = ''
	port = 5432


def _getDbConnectionSettings(DATABASE="store", SCHEMA=None):
	global rs_tunnel

	connectionSettings = ConnectionSettings()

	if DATABASE == "warehouse":
		connectionSettings.host_name = os.environ.get('WAREHOUSE_DB')
		connectionSettings.password = os.environ.get('POSTGRE_WAREHOUSE_P')
		connectionSettings.database = 'main_production'
		connectionSettings.user='postgres'
	elif DATABASE == "dev":
		connectionSettings.host_name = 'localhost'
		connectionSettings.password = 'mysecretpassword'
		connectionSettings.database = 'postgres'
		connectionSettings.user='postgres'
	elif DATABASE == "staging":
		connectionSettings.host_name = os.environ.get('STAGING_DB')
		connectionSettings.password = os.environ.get('POSTGRE_P2')
		connectionSettings.database = 'postgres'
		connectionSettings.user='postgres'
	elif DATABASE == "segment":
		connectionSettings.host_name = os.environ.get('SEGMENT_DB')
		connectionSettings.password = os.environ.get('SEGMENT_PW')
		connectionSettings.database = 'segment'
		connectionSettings.user = os.environ.get('SEGMENT_USER')
		connectionSettings.port = os.environ.get('SEGMENT_PORT')
	elif DATABASE == "redshift" or DATABASE == "heap" or DATABASE == "stitch":
		if os.environ.get('SSH_HOST'):
			try:
				rs_tunnel
			except NameError:
				rs_tunnel = CreateSSHTunnel(REMOTE=os.environ.get('REDSHIFT_HOST'), PORT=int(os.environ.get('REDSHIFT_PORT')))
				rs_tunnel.start()

			connectionSettings.port = rs_tunnel.local_bind_port
			connectionSettings.host_name = '127.0.0.1'
		else:
			connectionSettings.host_name = os.environ.get('REDSHIFT_HOST')
			connectionSettings.port = int(os.environ.get('REDSHIFT_PORT'))

		connectionSettings.user = os.environ.get('REDSHIFT_USER')
		connectionSettings.password = os.environ.get('REDSHIFT_PASS')
		if DATABASE == "redshift":
			connectionSettings.database = os.environ.get('REDSHIFT_DB')
		elif DATABASE == "stitch":
			connectionSettings.database = "stitch_data"
			connectionSettings.options = "-c search_path=hubspot" # set schema for stitch data. At the moment hardcoded to hubspot
		else:
			connectionSettings.database = "heap_db"
			connectionSettings.options = "-c search_path=main_production_clean"

		if not SCHEMA is None:
			connectionSettings.options = "-c search_path={}".format(SCHEMA)
	else:
		connectionSettings.host_name = os.environ.get('DATASTORE_DB')
		connectionSettings.password = os.environ.get('POSTGRE_P2')
		connectionSettings.database = 'postgres'
		connectionSettings.user='postgres'

	return connectionSettings



def _getDBConnector(DATABASE="store", SCHEMA=None, SETTINGS=None):
	"""! Connect to AWS postgres db"""
	import psycopg2	 # for PostgreSQL connections

	if not SETTINGS is None:
		connectionSettings = SETTINGS
	else:
		connectionSettings = GetDbConnectionSettings(DATABASE, SCHEMA=SCHEMA)

	mydb = psycopg2.connect(
		host=connectionSettings.host_name,
		user=connectionSettings.user,
		password=connectionSettings.password,
		database=connectionSettings.database,
		port=connectionSettings.port,
		options=connectionSettings.options
	)

	return mydb

#### SSH functions

def CreateSSHTunnel(REMOTE=None, PORT=3306):
	global tunnel

	import os
	import paramiko
	import sshtunnel

	if REMOTE is None:
		REMOTE = os.getenv("DBHOST")

	logging.debug('creating SSH tunnel to {}'.format(REMOTE))

	mypkey = paramiko.RSAKey.from_private_key_file('/Users/benjaminsmith/.ssh/' + 'id_rsa', password=os.getenv("SSH_PW"))

	tunnel = sshtunnel.SSHTunnelForwarder(
			(os.environ.get('SSH_HOST'), 22),
			ssh_username=os.getenv("SSH_USER"),
			ssh_password=os.getenv("SSH_PW"),
			ssh_pkey=mypkey,
			remote_bind_address=(REMOTE, PORT))

	tunnel.daemon_forward_servers = True # this was an idea to fix a connection hang, but it doesn't seem to matter.
	
	return tunnel

def CleanUpSSHTunnel():
	logging.debug('checking for SSH tunnels to cleanup...')
	global rs_tunnel, prod_tunnel

	try:
		tunnel
		tunnel.stop(force=True)
	except:
		pass

	try:
		prod_tunnel.stop(force=True)
	except:
		pass

	try:
		rs_tunnel.stop(force=True)
	except:
		pass

	# hack here: if we somehow lose a handle to an SSH tunnel it won't get shut down. So we look for paramiko transport threads and close them.
	import threading
	[t.close() for t in threading.enumerate() if t.__class__.__name__ == "Transport"]
