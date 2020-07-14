#Imports
##Standard Library
##Third Party
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from werkzeug.security import check_password_hash

##Local
from app.forms.functions import generate_where, required
from app.sql.functions import is_in_database

class Login_Form(FlaskForm):
	username = StringField('Username')
	password = PasswordField('Password')
	submit = SubmitField('Login')

	def check(self):
		print('check')
		self.id_user = -1
		user_data = {}
		excluded_fields = ['id_user']
		for a in vars(self):
			if (required(a, excluded_fields)):
				if (vars(self)[a].data == ''):
					self.user_data = {}
					return (False)
				else:
					user_data[a] = vars(self)[a].data
		
		user_data['id_user'] = 0
		where = generate_where('username', user_data['username'])
		results = is_in_database('users', user_data, where, return_results=True)
		print(results)
		if (results):
			user = {}

			for a in vars(self):
				if (required(a)):
					user[a] = results[0][a]

			print(user['password'])
			print(user_data['password'])
			if (check_password_hash(user['password'], user_data['password'])):
				self.id_user = user['id_user']
				print('YES')
				return (True)
			else:
				print("No")
				return (False)

		return (False)

	def login(self):
		##Set session id_user to id_user of the username
		session["id_user"] = self.id_user
		return (True)