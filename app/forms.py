from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class Registration_Form(FlaskForm):
	first_name = StringField('First name')
	last_name = StringField('Last name')
	username = StringField('Username')
	email = StringField('Email')
	password = PasswordField('Password')
	confirm_password = PasswordField('Confirm Password')
	submit = SubmitField('Register')

	def check(self):
		if (self.username.data):
			return (True)

class Login_Form(FlaskForm):
	username = StringField('Username')
	password = PasswordField('Password')