import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = './user_images'

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	MYSQL_HOST = 'localhost'
	MYSQL_USER = 'root'
	MYSQL_PASSWORD = '123456'
	MYSQL_DB = 'db_matcha'