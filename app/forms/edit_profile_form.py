#Imports
##Standard Library
##Third Party
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, FileField, SubmitField

##Local
from app.forms.fields import MultiCheckboxField
from app.forms.functions import calculate_id, is_in_array, required
from app.sql.functions import update_record, add_tags, remove_tags

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
		preferences = ['Male', 'Female']

		if (request.method != 'POST'):
			return (False)

		for a in vars(self):
			if (required(a, excluded_fields)):
				print('CHECK : ' + str(a))
				if (vars(self)[a].data == ''):
					return (False)
				else:
					altered_data = ""
					if (is_in_array(a, altered_fields)):
						altered_data = vars(self)[a].data
					if (a == 'preferences'):
						print('CALCULATE ID')
						altered_data = calculate_id(altered_data, preferences)
						print('id = ' + str(altered_data))
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
		bool_add : bool

		##Update the user data in database
		where = {
			'id_user' : session['id_user']
		}
		data = {}
		for field_name in self.user_data:
			print("Field : " + field_name)
			if (self.user_data[field_name] != vars(user)[field_name]):
				data[field_name] = self.user_data[field_name]

		print("Update user : " + str(data))
		update_record('users', data, where)
		print("tag_data : " + str(self.tag_data))
		tags_add = []
		tags_remove = []
		for form_tag in self.tag_data:
			print('FORM_TAG : ' + str(form_tag))
			bool_add = True
			for user_tag in user.tags:
				bool_add = False
				print('USER_TAG : ' + user_tag)
			
			if (bool_add):
				tags_add.append(form_tag)
		print('ADD TAGS : ' + str(tags_add))
		print('REMOVE TAGS' + str(tags_remove))
		add_tags(user.id_user, tags_add)
		remove_tags(user.id_user, tags_remove)
		##Remove old user images if they are overwritten
		##Add user images to the server
		return (True)