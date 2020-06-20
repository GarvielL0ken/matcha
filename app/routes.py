from flask import render_template, flash, redirect
from app import app
from app.forms import Registration_Form, Login_Form

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title="Home")

@app.route('/login')
def login():
	form = Login_Form()
	return (render_template('login.html', title="Login", form=form))

@app.route('/reset_password')
def reset_password():
	return (render_template('reset_password.html', title="Reset Password"))

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = Registration_Form()
	if (form.check()):
		flash('username {}, submit {}'.format(form.username.data, form.submit))
	return (render_template('register.html', title="Register", form=form))

@app.route('/profile')
def profile():
	return (render_template('profile.html', title="Profile"))

@app.route('/browse')
def browse():
	return (render_template('browse.html', title="Browse"))

@app.route('/chat')
def chat():
	return (render_template('chat.html', title="Chat"))

@app.route('/notifications')
def notifications():
	return (render_template('notifications.html', title="Notifications"))