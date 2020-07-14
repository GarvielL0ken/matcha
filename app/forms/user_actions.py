#Imports
##Standard Library
##Third Party
from flask_wtf import FlaskForm
from wtforms import SubmitField
from werkzeug.security import check_password_hash, generate_password_hash

##Local
from app.forms.functions import required
from app.sql.functions import insert_record

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