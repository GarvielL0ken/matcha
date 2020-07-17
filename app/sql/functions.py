from datetime import date, datetime, timedelta
from app.sql.setup import get_connection
import mysql.connector
from random import getrandbits

def data_to_column(data, format_codes=False, brackets=True, paired=False):
	columns : str
	i : int

	i = 0
	columns = ""

	if (brackets):
		columns = "("

	for column_name in data:
		if (i):
			columns += ", "
		if (paired):
			columns += column_name + " = "
		if (format_codes):
			columns += "%("
		columns += column_name
		if (format_codes):
			columns += ")s"
		i += 1

	if (brackets):
		columns += ")"

	return (columns)

def	execute_sql(sql, data={}, return_id=False, query=False, dictionary=False):
	print(sql)
	print(str(data))
	conn = get_connection(dictionary)
	cnx = conn['connection']
	cursor = conn['cursor']
	cursor.execute(sql, data)
	if (query):
		results = cursor.fetchall()
		cursor.close()
		cnx.close()
		return (results)
	else:
		cnx.commit()
		last_id = cursor.lastrowid
		cursor.close()
		cnx.close()

	if (return_id):
		return (last_id)
	else:
		return (0)

def insert_record(table, data, return_id=False):
	sql : str

	sql = "INSERT INTO `" + table + "` "
	sql += data_to_column(data)
	sql += " VALUES "
	sql += data_to_column(data, True)
	#print(sql)
	id_user = execute_sql(sql, data)
	if (return_id):
		return (id_user)
	else:
		return (0)

def insert_hash(column, id_user):
	hash = getrandbits(128)
	data = {
		'id_user' : id_user,
		column : hash
	}
	insert_record('hashes', data)

def insert_verification_hash(id_user):
	insert_hash('verification', id_user)

def insert_new_password_hash(id_user):
	insert_hash('reset_password', id_user)

def get_results(table, data={}, where={}, all=False, order_by={}):
	sql = "SELECT "
	if (all):
		sql += "*"
	else:
		sql += data_to_column(data, brackets=False)
	sql += " FROM " + table
	if (where):
		sql += " WHERE "
		sql += where['column'] + " = %(value)s"
		data['value'] = where['value']
	if (order_by):
		sql += " ORDER BY "
		sql += order_by['column'] + " " + order_by['order']

	results = execute_sql(sql, data, query=True, dictionary=True)
	#print(results)
	return (results)

def get_id_user(column, value):
	data = {}
	data['id_user'] = 0
	where = {
		'column' : column,
		'value' : value
	}

	results = get_results('users', data, where)
	id_user = results[0]['id_user']
	print("get_id_user(" + column + ", " + value + ") : " + str(id_user))
	return (id_user)

def is_in_database(table, data, where, return_results=False):
	results = get_results(table, data, where)
	if (results):
		if (return_results):
			return (results)
		else:
			return (True)
	else:
		return (False)

def update_record(table, data, where={}):
	sql = "UPDATE " + table
	sql += " SET "
	sql += data_to_column(data, format_codes=True, brackets=False, paired=True)
	sql += " WHERE "
	sql += data_to_column(where, format_codes=True, brackets=False, paired=True)
	print(sql)
	for column in where:
		data[column] = where[column]
	execute_sql(sql, data)
	return (True)

def get_like_status(id_user_1, id_user_2):
	sql = 'SELECT * ' 
	sql += 'FROM likes ' 
	sql += 'WHERE '
	sql += '(id_user_1 = %(id_user_1)s AND id_user_2 = %(id_user_2)s) '
	sql += 'OR (id_user_1 = %(id_user_2)s AND id_user_2 = %(id_user_1)s)'
	data = {
		'id_user_1' : id_user_1,
		'id_user_2' : id_user_2
	}
	results = execute_sql(sql, data, query=True, dictionary=True)
	if (results):
		result = results[0]
		return (result)
	else:
		return (False)

def get_matched_users(id_user):
	sql = 'SELECT * FROM `likes` '
	sql += 'WHERE (id_user_1 = %(id_user)s OR id_user_2 = %(id_user)s) '
	sql += 'AND (user_1_like = 1 AND user_2_like = 1)'
	data = {
		'id_user' : id_user
	}
	results = execute_sql(sql, data, query=True, dictionary=True)
	matched_users = []
	i = 0
	for result in results:
		column = 'id_user_1'
		if (id_user == result[column]):
			column = 'id_user_2'
		matched_users.append(result[column])
		i += 1

	return (matched_users)

def get_messages_db(id_user_1, id_user_2):
	sql = 'SELECT * FROM messages '
	sql += 'WHERE (id_user_from = %(id_user_1)s AND id_user_to = %(id_user_2)s) '
	sql += 'OR (id_user_to = %(id_user_2)s AND id_user_from = %(id_user_1)s)	'
	data = {
		'id_user_1' : id_user_1,
		'id_user_2' : id_user_2
	}
	results = execute_sql(sql, data, query=True, dictionary=True)
	if (not results):
		return (False)
	else:
		return (results)

def update_like_status_db(data):
	sql = 'UPDATE likes '
	sql += 'SET '
	sql += data_to_column(data, format_codes=True, brackets=False, paired=True)
	sql += ' WHERE '
	sql += '(id_user_1 = %(id_user_1)s AND id_user_2 = %(id_user_2)s) '
	sql += 'OR (id_user_1 = %(id_user_2)s AND id_user_2 = %(id_user_1)s)'
	execute_sql(sql, data)

def remove_record(table, where, data):
	sql = 'DELETE FROM ' + table
	sql += ' WHERE ' + where
	execute_sql(sql, data)
#data = {
#	'username' : "Not Garviel",
#	'first_name' : "John"
#}

#where= {
#	'column' : 'id_user',
#	'value' : 2
#}

#where = {
#	'id_user' : 2
#}

#update_record('users', data, where)
##get_id_user('afjnasf')
#insert_record('users', data)
##execute_sql(sql_user, data_user)
#is_in_database('users', data, where)
