#imports

##Standard Library

##Third Party
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from werkzeug.security import generate_password_hash

##Local
from app.forms.functions import required
from app.sql.functions import insert_record, insert_verification_hash

class Registration_Form(FlaskForm):
	first_name = StringField('First name')
	last_name = StringField('Last name')
	username = StringField('Username')
	email = StringField('Email')
	password = PasswordField('Password')
	confirm_password = PasswordField('Confirm Password')
	submit = SubmitField('Register')

	def check(self):
		user_data = {}
		excluded_fields = ['confirm_password']
		for a in vars(self):
			if (required(a, excluded_fields)):
				if (vars(self)[a].data == ''):
					self.user_data = {}
					return (False)
				else:
					user_data[a] = vars(self)[a].data
		print(user_data['password'])
		user_data['password'] = generate_password_hash(user_data['password'])
		print(user_data['password'])
		self.user_data = user_data
		return (True)

	def add_user(self):
		##Add user to database
		id_user = insert_record('users', self.user_data, True)
		##Add a verification hash to database
		insert_verification_hash(id_user)
		##Send verification hash to user via email
		##Flash a message for the user
		##Redirect to login
		return (True)