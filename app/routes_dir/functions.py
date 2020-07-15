#imports
##Standard Library
##Third Party
from flask import session

##Local
from app.models import User
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
	where = calculate_preferences(user.preferences, ['M', 'F'])
	where['column'] = 'gender'
	order_by = {
		'column' : 'intrigue',
		'order' : 'DESC'
	}
	if (not where['value']):
		where = {}
	lst_users = get_results('users', {}, where, all=True, order_by=order_by)
	return (lst_users)

def get_logged_in_user():
	user = False
	if (session):
		if (session['id_user'] != 0):
			user = User(session['id_user'])
	return (user)