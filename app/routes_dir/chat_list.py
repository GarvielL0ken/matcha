#imports
##Standard Library
##Third Party
from flask import redirect, render_template, session, url_for

##Local
from app import app
from app.models import User
from app.sql.functions import get_messages, get_matched_users
from app.routes_dir.functions import get_logged_on_user

@app.route('/chat', methods=['GET', 'POST'])
def chat():
	##Redirect if not logged in
	user = get_logged_on_user()
	if (not user):
		return redirect(url_for('login'))

	##Get all users that have a chat with the current user
	matched_users = get_matched_users(user.id_user)
	messages = []
	print("Matched_users : " + str(matched_users))
	for id_user in matched_users:
		messages.append(user.get_messages(id_user))
	print('Messages : ' + str(messages)
	messages = False
	return (render_template('chat.html', title="Chat", messages=messages, user=user))