#imports

##Standard Library

##Third Party
from flask import render_template

##Local
from app import app
from app.routes_dir import browse, chat, chat, login, logout, notifications, profile, register, reset_password, user

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title="Home")