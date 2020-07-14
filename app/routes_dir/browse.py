#imports

##Standard Library

##Third Party
from flask import redirect, render_template, session, url_for

##Local
from app import app
from app.models import User

@app.route('/browse', methods=['GET', 'POST'])
def browse():
	##Redirect if not logged in
	if (session['id_user'] == 0):
		return redirect(url_for('login'))

	lst_users = []
	u = User(1)
	lst_users.append(u.data_to_dict('min'))
	u = User(2)
	lst_users.append(u.data_to_dict('min'))
	return (render_template('browse.html', title="Browse", users=lst_users))