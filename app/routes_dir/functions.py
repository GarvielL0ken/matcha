#imports
##Standard Library
##Third Party
##Local
from app.sql.functions import get_results

def calculate_preferences(preference, arr_options):
	where = {}
	where['value'] = ''
	if (preference == 1):
		where['value'] = 'M'
	elif (preference == 2):
		where['value'] = 'F'
	return (where)

def get_users(user):
	lst_users = []
	print(user.preferences)
	where = calculate_preferences(user.preferences, ['M', 'F'])
	where['column'] = 'gender'
	order_by = {
		'column' : 'intrigue',
		'order' : 'DESC'
	}
	print(where)
	if (not where['value']):
		where = {}
	print(where)
	lst_users = get_results('users', {}, where, all=True, order_by=order_by)
	print(lst_users)
	return (lst_users)