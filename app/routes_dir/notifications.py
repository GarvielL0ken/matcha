#imports
##Standard Library
##Third Party
from flask import redirect, render_template, session, url_for

##Local
from app import app

@app.route('/notifications', methods=['GET', 'POST'])
def notifications():
	##Redirect if not logged in
	try:
		if (session['id_user'] != 0):
			user = User(session['id_user'])
	except:
		return redirect(url_for('login'))
	
	notifications = user.get_notifications()
	return (render_template('notifications.html', title="Notifications", notifications=notifications))