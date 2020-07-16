from app.sql.function import get_like_status

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
	#Determine whether user_2 has already liked user_1
	##Update the appropraite record if it already exists
	##Otherwise insert anew record
	data = {
		'id_user_1' : id_user_1,
		'id_user_2' : id_user_2,
		'user_1_like' : True,
		'user_2_like' : False
	}

	like_status = get_like_status(id_user_1, id_user_2)
	user_2_like = False
	if (like_status):
		if (id_user_1 == like_status['id_user_1']):
			user_2_like = like_status['user_2_like']
		else:
			user_2_like = like_status
	else:
		insert_record('likes', data)