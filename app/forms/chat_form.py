#Imports
##Standard Library
from datetime import datetime

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
		valid = False
		if (request.method == 'POST'):
			if (self.message.data):
				if (self.submit.data):
					valid = True
		return (valid)

	def send_message(self, user_from, user_to):
		obj_now = datetime.now()
		str_now = obj_now.strftime('%Y/%m/%d %H:%M:%S')
		data = {
			'id_user_from' : user_from,
			'id_user_to' : user_to,
			'message' : self.message.data,
			'time_sent' : str_now
		}
		insert_record('messages', data)