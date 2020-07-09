import mysql.connector
from mysql.connector import errorcode
from database import config, DB_NAME, TABLES

def get_connection():
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	cursor.execute("USE {}".format(DB_NAME))

	result = {
		'connection' : cnx,
		'cursor' : cursor
	}
	return (result)

def	execute_sql(sql, data={}, return_id=False):
	conn = get_connection()
	cnx = conn['connection']
	cursor = conn['cursor']
	cursor.execute(sql, data)
	cnx.commit()
	last_id = cursor.lastrowid
	cursor.close()
	cnx.close()
	if (return_id):
		return (last_id)
	else:
		return (0)

def drop_table(table):
	sql = "DROP TABLE " + table
	execute_sql(sql)

#drop_table('users')
#drop_table('hashes')
#drop_table('tags')
#drop_table('tag_map')
