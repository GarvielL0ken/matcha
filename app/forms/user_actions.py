#Imports
##Standard Library
##Third Party
from flask_wtf import FlaskForm
from wtforms import SubmitField
from werkzeug.security import check_password_hash, generate_password_hash

##Local
from app.forms.functions import required
from app.sql.functions import insert_record

class User_Actions_Form(FlaskForm):
	like = SubmitField('Like')
	unlike = SubmitField('Unlike')
	block = SubmitField('Block')
	report = SubmitField('Report as fake')

	def check(self):
		for a in vars(self):
			if (required(a)):
				if (vars(self)[a].data == ''):
					return (False)
		return (True)

	def perform_action(self, action, current_user, viewed_user):
		if (action == 'like'):
			if (user_already_liked(current_user.id_user, viewed_user.id_user)):
				match_users(current_user.id_user, viewed_user.id_user)
			else
				add_like(current_user.id_user, viewed_user.id_user)
		elif (action == 'unlike'):
			if (users_connected(current_user.id_user, viewed_user.id_user)):
				disconnect_users(current_user.id_user, viewed_user.id_user)
			else:
				remove_like(current_user.id_user, viewed_user.id_user)
		elif (action == 'block'):
			data = {
				'user_blockee' : current_user.id_user,
				'user_blocked' : viewed_user.id_user
			}
			insert_record('blocked_user', data)
		elif (action == 'report'):
			data = {
				'user_reported' : viewed_user.id_user
			}
			insert_record('reported_users', data)
		return (True)