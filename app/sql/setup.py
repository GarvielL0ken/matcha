import mysql.connector
from mysql.connector import errorcode
from app.sql.database import config, DB_NAME, TABLES

def create_database(cursor):
	try:
		cursor.execute(
			"CREATE DATABASE {}".format(DB_NAME))
	except mysql.connector.Error as err:
		print("Failed creating database: {}".format(err))
		exit(1)

def get_connection(dictionary):
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor(dictionary=dictionary)

	##	Attempt to establish a connection with the database
	##	If the database does not exist, create the database
	##	Otherwise display an error message and exit the program
	try:
		cursor.execute("USE {}".format(DB_NAME))
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database {} does not exist.".format(DB_NAME))
			create_database(cursor)
			print("Database {} created.".format(DB_NAME))
			cnx.database = DB_NAME
		else:
			print(err)

	for table_name in TABLES:
		table_description = TABLES[table_name]
		try:
			print("Creating table {}: ".format(table_name), end='')
			cursor.execute(table_description)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
				print("already exists.")
			else:
				print(err.msg)
		else:
			print("OK")

	result = {
		'connection' : cnx,
		'cursor' : cursor
	}
	return (result)