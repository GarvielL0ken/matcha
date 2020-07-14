#imports
##Standard Library

##Third Party
from flask import redirect, render_template, session, url_for
##Local

from app import app

@app.route('/chat/<username>', methods=['GET', 'POST'])
def chat_user(username):
	##Redirect if not logged in
	if (session['id_user'] == 0):
		return redirect(url_for('login'))

	return (render_template('chat.html', title="Chat", username=username))