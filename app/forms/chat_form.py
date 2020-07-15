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

class Chat_Form(FlaskForm):
	message = TextAreaField('Message')
	submit = SubmitField('Send Message')