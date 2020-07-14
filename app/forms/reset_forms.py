#Imports
##Standard Library
##Third Party
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from werkzeug.security import check_password_hash, generate_password_hash

##Local
from app.forms.functions import required
from app.sql.functions import get_id_user, insert_new_password_hash, update_record

class Reset_Password_Email_Form(FlaskForm):
	email = StringField('Email')
	submit = SubmitField('Send Link')

	def check(self):
		for a in vars(self):
			if (required(a)):
				if (vars(self)[a].data == ''):
					return (False)
		return (True)

	def send_reset_email(self):
		##Store a hash in database
		id_user = get_id_user('email', vars(self)['email'])
		insert_new_password_hash(id_user)
		##Send the hash to the user via email
		##Flash a message for the user
		##Redirect to reset_password?action=message
		return (True)

class Reset_Password_Form(FlaskForm):
	password = PasswordField('Password')
	confirm_password = PasswordField('Confirm Password')
	submit = SubmitField('Reset Password')

	def check(self):
		self.user_data = {}
		user_data = {}
		excluded_fields = ['confirm_password']
		for a in vars(self):
			if (required(a, excluded_fields)):
				if (vars(self)[a].data == ''):
					self.user_data = {}
					return (False)
				else:
					user_data[a] = vars(self)[a].data
		user_data['password'] = generate_password_hash(user_data['password'])
		self.user_data = user_data

	def reset_password(self):
		##Update users password in database
		where = {
			'id_user' : self.id_user
		}
		update_record('users', self.user_data, where)
		##Flash a message for the user
		##Redirect to login
		return (True)
