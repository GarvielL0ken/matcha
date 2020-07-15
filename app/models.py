from app.sql.functions import get_results
from app.forms.functions import required

class User():
	def __init__(self, id_user, username=''):
		column : str

		if (username):
			column = 'username'
			value = username
		else:
			column = 'id_user'
			value = id_user

		where = {
			'column' : column,
			'value' : value
		}
		results = get_results('users', {}, where, all=True)
		user = results[0]
		#print(user)
		for column_name in user:
			#print(column_name)
			#print(user[column_name])
			setattr(self, column_name, user[column_name])

	def set_message(self, message, time_sent):
		self.message = message
		self.time_sent = time_sent

	def data_to_dict(self, method):

		#if (method == 'chat_preview'):
		#	data = {
		#		'username' : self.username,
		#		'message' : self.message,
		#		'time_sent' : self.time_sent
		#	}
		#if (method == 'min'):
		#	data = {
		#		'username' : self.username,
		#		'age' : self.age,
		#		'gender' : self.gender,
		#		'fame_rating' : self.fame_rating,
		#		'profile_pictures' : self.pictures
		#	}
		#if (method == 'view'):
		#	data = {
		#		'username' : self.username,
		#		'first_name' : self.first_name,
		#		'last_name' : self.last_name,
		#		'age' : self.age,
		#		'gender' : self.gender,
		#		'fame_rating' : self.fame_rating,
		#		'preferences' : self.preferences,
		#		'bio' : self.bio,
		#		'tags' : self.tags,
		#		'profile_pictures' : self.pictures,
		#		'online_status' : self.online_status,
		#		'like_status' : self.like_status,
		#	}
		#if (method == 'profile'):
			#data = {
			#	'username' : self.username,
			#	'first_name' : self.first_name,
			#	'last_name' : self.last_name,
			#	'email' : self.email,
			#	'age' : self.age,
			#	'gender' : self.gender,
			#	'fame_rating' : self.fame_rating,
			#	'preferences' : self.preferences,
			#	'bio' : self.bio,
			#	'tags' : self.tags,
			#	'profile_pictures' : self.pictures,
			#	'liked_by' : self.liked_by,
			#	'viewed_by' : self.viewed_by,
			#	'location' : self.location
			#}
		user = {}
		for a in vars(self):
			if (required(a)):
				gender = ''
				if (a == 'gender'):
					if (vars(self)[a] == 'M'):
						gender = 'Male'
					elif (vars(self)[a] == 'F'):
						gender = 'Female'
				if (a == 'preferences'):
					if (self.preferences):
						user[a] = self.preferences_int_to_array()
				elif (gender):
					user[a] = gender
				else:
					user[a] = vars(self)[a]
		return (user)

	def get_notifications(self):
		notifications = []
		return (notifications)

	def browse_users(self):
		users = get_results('users', all=True)
		return (users)

	def preferences_int_to_array(self):
		arr_preferences = []
		print("Pref to array : preference : " + str(self.preferences))
		print(self.preferences % 2)
		print((self.preferences >> 1) % 2)
		if (self.preferences % 2):
			arr_preferences.append('Male')
		if ((self.preferences >> 1) % 2):
			arr_preferences.append('Female')
		return (arr_preferences)
