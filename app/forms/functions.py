from app.sql.functions import get_like_status, insert_record, update_like_status_db, remove_record

def calculate_id(arr_elements, arr_options):
	int_id : int
	int_order : int

	int_id = 0
	int_order = 1
	for option in arr_options:
		for element in arr_elements:
			if (element == option):
				int_id = int_id + int_order
				break
		int_order = int_order * 2
	return (int_id)

def generate_where(column, value):
	where = {
		'column' : column,
		'value' : value
	}
	return (where)

def is_in_array(string : str, array=[]):
	for element in array:
		if (string == element):
			return (True)
	return(False)

def required(a, excluded_fields=[]):
	if (a == 'submit' or a == "meta" or a == "_prefix" or a == "_fields" or a == "_csrf" or a == "csrf_token"):
		return (False)
	for field in excluded_fields:
		if (a == field):
			return (False)
	return (True)

def add_like(id_user_1, id_user_2):
	update_like_status(id_user_1, id_user_2, action='add')

def remove_like(id_user_1, id_user_2):
	update_like_status(id_user_1, id_user_2, 'remove')

def update_like_status(id_user_1, id_user_2, action='add'):
	data = {
		'id_user_1' : id_user_1,
		'id_user_2' : id_user_2,
		'user_1_like' : True,
		'user_2_like' : False
	}
	if (action == 'remove'):
		data['user_1_like'] = False

	like_status = get_like_status(id_user_1, id_user_2)
	if (like_status):
		if (id_user_1 == like_status['id_user_1']):
			data['user_2_like'] = like_status['user_2_like']
		else:
			data['user_2_like'] = like_status['user_1_like']

		if (action == 'add' or data['user_2_like']):
			update_like_status_db(data)
		elif (action == 'remove'):
			where = '(id_user_1  = %(id_user_1)s AND id_user_2 = %(id_user_2)s) OR (id_user_1 = %(id_user_2)s AND id_user_2 = %(id_user_2)s)'
			remove_record('likes', where, data)

	else:
		if (action == 'add'):
			insert_record('likes', data)
	return (True)