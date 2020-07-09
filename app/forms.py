from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, DateField, SelectMultipleField, TextAreaField, FileField, widgets
from wtforms.widgets import TextArea
from werkzeug.security import generate_password_hash, check_password_hash
from app.sql.functions import insert_record, insert_verification_hash, insert_new_password_hash, get_id_user, update_record, is_in_database
from flask import session

def required(a, excluded_fields=[]):
	if (a == 'submit' or a == "meta" or a == "_prefix" or a == "_fields" or a == "_csrf" or a == "csrf_token"):
		return (False)
	for field in excluded_fields:
		if (a == field):
			return (False)
	return (True)

def generate_where(column, value):
	where = {
		'column' : column,
		'value' : value
	}
	return (where)

class MultiCheckboxField(SelectMultipleField):
	widget = widgets.ListWidget(prefix_label=False)
	option_widget = widgets.CheckboxInput()

class MultiFileField():
	def __init__(self, labels):
		self.files = {}
		for label in labels:
			self.files[label] = FileField(label)

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

class User_Data_Form(FlaskForm):
	first_name = StringField('First name')
	last_name = StringField('Last name')
	username = StringField('Username')
	email = StringField('Email')
	gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
	preferences = MultiCheckboxField('Preferences', choices=[('male', 'Male'), ('female', 'Female')])
	age = DateField('Date of Birth', format='%d/%m/%Y')
	bio = TextAreaField('Bio')
	tags = TextAreaField('Tags')
	location = StringField('Location')
	pict_0 = FileField('0')
	pict_1 = FileField('1')
	pict_2 = FileField('2')
	pict_3 = FileField('3')
	pict_4 = FileField('4')
	submit = SubmitField('Change Info')

	def check(self):
		self.user_data = {}
		user_data = {}
		excluded_fields = ['pict_1', 'pict_2', 'pict_3', 'pict_4']
		for a in vars(self):
			if (required(a, excluded_fields)):
				if (vars(self)[a].data == ''):
					self.user_data = {}
					return (False)
				else:
					user_data[a] = vars(self)[a].data
		user_data['password'] = generate_password_hash(user_data['password'])
		self.user_data = user_data

	def update_user_data(self):
		##Update the user date in database
		where = {
			'id_user' : session['id_user']
		}
		update_record('users', self.user_data, where)
		##Remove old user images if they are overwritten
		##Add user images to the server
		return (True)

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

	def perform_action(self, action):
		##Case Action:
		##	Like:
		##		add a new record to the database for the two users
		##		Add a new Notification in the database for the liked user
		##	Unlike:
		##		Update the like status in the database
		##		Remove the record if neither user likes the other
		##	Block:
		##		Add a record to the database
		insert_record('blocked_users', self.data)
		##	Report:
		##		Add a record to the database for admin review
		insert_record('reported_users', self.data)
		return (True)