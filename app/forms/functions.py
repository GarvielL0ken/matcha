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