#imports
##Standard Library
from datetime import date, datetime

##Third Party

##Local
from app.sql.functions import get_results, get_like_status, get_messages_db, get_number, update_status
from app.forms.functions import required

class User():
	def __init__(self, id_user=0, username=''):
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

		self.calculate_age()
		self.calculate_fame_rating()
		#self.set_views()
		#self.set_likes()

	def calculate_age(self):
		dob = self.dob
		today = date.today()
		age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)) 

		self.age = age
		return (True)

	def calculate_fame_rating(self):
		##Calculate how popular a user is based on the following factors
		l : int	#Number of likes
		u : int	#Number of users
		v : int #Number of views

		##fame rating = LUV
		##LUV = acceptance rate + surface appeal
		##   like to view ratio + views
		##acceptance rate needs to scale with the number of users:
		##LUV = (l / v * u) + v
		##Denominator : (v) => (v + (v == 0)) if v == 0 then v += 1

		l = get_number(self.id_user, 'likes')
		u = get_number(self.id_user, 'users', number_of_records=True)
		v = get_number(self.id_user, 'views')

		fame_rating = (l / (v + (v == 0))) * u + v
		self.fame_rating = fame_rating

	def determine_like_status(self, id_user):
		print("Detemine Like Status")
		like_status = get_like_status(self.id_user, id_user)
		print('Like Status : ' + str(like_status))

		if (not like_status):
			print("Record Does not exist")
			self.like_status = [0, '']
			return (True)

		#Determine which user the viewed user is
		column_self = 'user_1_like'
		column_user = 'user_2_like'
		if (self.id_user == like_status['id_user_2']):
			column_self = 'user_2_like'
			column_user = 'user_1_like'
		
		arr_like_status = [0, '']
		if (like_status[column_user]):
			arr_like_status[0] = 1
		if (like_status[column_self]):
			arr_like_status[1] = 'Likes You'
		
		self.like_status = arr_like_status
		return (True)

	def get_messages(self, id_user_2, return_messages=False, return_most_recent=False):
		messages = get_messages_db(self.id_user, id_user_2)
		if (return_messages):
			if (return_most_recent):
				if (messages):
					key = lambda message : message['time_sent']
					messages = sorted(messages, key=key, reverse=True)
					messages = messages[0]
			return (messages)
		else:
			self.messages = messages

	def set_attribute(self, table):
		column : str
		
		attribute = table[:-1]
		where = {
			'id_user_1' : 'id_user',
			'_C0' : 'OR',
			'id_user_2' : 'id_user',
		}
		data = {
			'id_user' : self.id_user
		}
		results = get_results(table, data, where=where, all=True, compound_condition=True)

		arr_by = []
		for record in results:
			column = 'user_2'
			if (self.id_user != record['id_user_1']):
				column = 'user_1'
			if (record[column + '_' + attribute]):
				arr_by.append(User(record['id_' + column]))
		
		return (arr_by)

	def set_views(self):
		self.viewed_by = self.set_attribute('views')
		
	def set_likes(self):
		self.liked_by = self.set_attribute('likes')

	def view_user(self, id_user):
		update_status(self.id_user, id_user, 'views')
		return (True)

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
