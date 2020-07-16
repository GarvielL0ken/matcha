#Imports
##Standard Library
##Third Party
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, FileField, SubmitField

##Local
from app.forms.fields import MultiCheckboxField
from app.forms.functions import calculate_id, is_in_array, required
from app.sql.functions import update_record

class Edit_Profile_Form(FlaskForm):
	first_name = StringField('First name')
	last_name = StringField('Last name')
	username = StringField('Username')
	email = StringField('Email')
	gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
	preferences = MultiCheckboxField('Preferences', choices=[('Male', 'Male'), ('Female', 'Female')])
	dob = StringField('Date of Birth, yyyy/mm/dd')
	bio = TextAreaField('Bio')
	tags = TextAreaField('Tags')
	location = StringField('Location')
	pict_0 = FileField('0')
	pict_1 = FileField('1')
	pict_2 = FileField('2')
	pict_3 = FileField('3')
	pict_4 = FileField('4')
	submit = SubmitField('Change Info')

	def check(self, request):
		self.user_data = {}
		self.tag_data = []
		user_data = {}

		excluded_fields = ['pict_0', 'pict_1', 'pict_2', 'pict_3', 'pict_4', 'user_data', 'tag_data', 'location']
		altered_fields = ['preferences']
		preferences = ['male', 'female']

		if (request.method != 'POST'):
			return (False)

		for a in vars(self):
			if (required(a, excluded_fields)):
				print(a)
				if (vars(self)[a].data == ''):
					return (False)
				else:
					altered_data = ""
					if (is_in_array(a, altered_fields)):
						altered_data = vars(self)[a].data
					if (a == 'preferences'):
						altered_data = calculate_id(altered_data, preferences)
					if (altered_data):
						print("altered_data : " + str(altered_data))
						user_data[a] = altered_data
					elif (a == 'tags'):
						self.tag_data = vars(self)[a].data.split("#")
						if (not self.tag_data[0]):
							del self.tag_data[0]
					else:
						user_data[a] = vars(self)[a].data

		self.user_data = user_data
		return (True)

	def update_user_data(self, request, user):
		##Update the user data in database
		where = {
			'id_user' : session['id_user']
		}
		data = {}
		for field_name in self.user_data:
			print("Field : " + field_name)
			try:
				if (self.user_data[field_name] != vars(user)[field_name]):
					data[field_name] = self.user_data[field_name]
			except:
				data[field_name] = self.user_data[field_name]

		print("Update user : " + str(self.user_data))
		update_record('users', self.user_data, where)
		##Remove old user images if they are overwritten
		##Add user images to the server
		return (True)