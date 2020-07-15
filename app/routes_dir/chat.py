#imports
##Standard Library

##Third Party
from flask import redirect, render_template, request, session, url_for

##Local
from app import app
from app.forms.chat_form import Chat_Form
from app.sql.functions import get_id_user

@app.route('/chat/<username>', methods=['GET', 'POST'])
def chat_user(username):
	##Redirect if not logged in
	try:
		if (session['id_user'] != 0):
			user = User(session['id_user'])
	except:
		return redirect(url_for('login'))

	##Get user
	id_user_to = get_id_user('username', username)

	##Send a message if prompted
	form = Chat_Form()
	if (form.check()):
		form.send_message(session['id_user'], id_user_to=id_user_to)

	##Get all user messages
	messages = get_messages(session['id_user'], id_user_to)

	return (render_template('chat.html', title="Chat", username=username, form=form, messages=messages))