#imports
##Standard Library
##Third Party
from flask import redirect, render_template, session, url_for

##Local
from app import app
from app.models import User

@app.route('/chat', methods=['GET', 'POST'])
def chat():
	##Redirect if not logged in
	try:
		if (session['id_user'] != 0):
			user = User(session['id_user'])
	except:
		return redirect(url_for('login'))

	##Get all users that have a chat with the current user
	messages = get_messages(session['id_user'], method='summary')
	return (render_template('chat.html', title="Chat", messages=messages))