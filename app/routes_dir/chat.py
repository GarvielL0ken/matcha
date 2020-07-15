#imports
##Standard Library

##Third Party
from flask import redirect, render_template, request, session, url_for

##Local
from app import app
from app.forms.chat_form import Chat_Form
from app.sql.functions import get_id_user
from app.routes_dir.functions import get_logged_in_user

@app.route('/chat/<username>', methods=['GET', 'POST'])
def chat_user(username):
	print('Logged In?')
	print(str(session['id_user']))
	##Redirect if not logged in
	user = get_logged_in_user()
	if (not user):
		return redirect(url_for('login'))

	##Get user
	id_user_to = get_id_user('username', username)

	##Send a message if prompted
	form = Chat_Form()
	if (form.check(request)):
		form.send_message(session['id_user'], id_user_to=id_user_to)

	##Get all user messages
	##messages = get_messages(session['id_user'], id_user_to)

	return (render_template('chat.html', title="Chat", username=username, form=form, user=user))