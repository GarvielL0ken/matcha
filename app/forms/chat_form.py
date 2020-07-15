#Imports
##Standard Library
from datetime import date

##Third Party
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, FileField, SubmitField

##Local
from app.forms.fields import MultiCheckboxField
from app.forms.functions import calculate_id, is_in_array, required
from app.sql.functions import update_record, insert_record

class Chat_Form(FlaskForm):
	message = TextAreaField('Message')
	submit = SubmitField('Send Message')

	def check(self, request):
		if (request.method != 'POST'):
			return (False)
		if (not self.message.data):
			return (False)
		return (True)

	def send_message(self, user_from, user_to):
		print(date.today())
		data = {
			'user_from' : user_from,
			'user_to' : user_to,
			'message' : self.message.data
		}
		#insert_record('messages', )