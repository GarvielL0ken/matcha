#imports

##Standard Library

##Third Party
from flask import redirect, render_template, session, url_for

##Local
from app import app
from app.models import User
from app.routes_dir.functions import get_users

@app.route('/browse', methods=['GET', 'POST'])
def browse():
	##Redirect if not logged in
	try:
		if (session['id_user'] != 0):
			user = User(session['id_user'])
	except:
		return redirect(url_for('login'))

	##Pagination

	##Get users based on the user preference and gender
	lst_users = user.browse_users()
	return (render_template('browse.html', title="Browse", users=lst_users))