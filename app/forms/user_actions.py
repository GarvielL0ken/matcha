#Imports
##Standard Library
##Third Party
from flask_wtf import FlaskForm
from wtforms import SubmitField
from werkzeug.security import check_password_hash, generate_password_hash

##Local
from app.forms.functions import required, add_like, remove_like
from app.sql.functions import insert_record, is_in_database, update_record

class User_Actions_Form(FlaskForm):
	like = SubmitField('Like')
	unlike = SubmitField('Unlike')
	block = SubmitField('Block')
	report = SubmitField('Report as fake')

	def check(self, current_user, viewed_user):
		for a in vars(self):
			if (required(a)):
				if (vars(self)[a].data):
					self.perform_action(a, current_user, viewed_user)
		return (True)

	def perform_action(self, action, current_user, viewed_user):
		if (action == 'like'):
			add_like(current_user.id_user, viewed_user.id_user)
		elif (action == 'unlike'):
			remove_like(current_user.id_user, viewed_user.id_user)
		elif (action == 'block'):
			data = {
				'user_blockee' : current_user.id_user,
				'user_blocked' : viewed_user.id_user
			}
			insert_record('blocked_user', data)
		elif (action == 'report'):
			data = {
				'id_user' : viewed_user.id_user
			}
			where = {
				'column' : 'id_user',
				'value' : viewed_user.id_user
			}
			results = is_in_database('reported_users', {}, where, return_results=True)
			if (results):
				result = results[0]
				data['number_of_reports'] = result['number_of_reports'] + 1
				update_record('reported_users', data, where)
			insert_record('reported_users', data)
		return (True)