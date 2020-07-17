#imports
##Standard Library
##Third Party
from flask import redirect, render_template, request, session, url_for

##Local
from app import app
from app.models import User
from app.forms.chat_form import Chat_Form
from app.sql.functions import get_matched_users
from app.routes_dir.functions import get_logged_on_user

@app.route('/chat', methods=['GET', 'POST'])
def chat():
	##Redirect if not logged in
	user = get_logged_on_user()
	if (not user):
		return redirect(url_for('login'))

	action = request.args.get('action')
	if (action == 'chat'):
		username = request.args.get('username')
		if (not username):
			action = 'list'

	if (action != 'chat'):
		##Get all users that have a chat with the current user and their messages
		matched_users = get_matched_users(user.id_user)
		users = []
		i = 0
		for id_user in matched_users:
			users.append(User(id_user))
			users[i].messages = user.get_messages(id_user, return_messages=True, return_most_recent=True)
			print("User messages : " + str(users[i].messages))
			i += 1

		##Convert array of users into array of dicts
		dict_users = []
		for u in users:
			dict_users.append(u.data_to_dict('preview'))
		return (render_template('chat.html', title="Chat", user=user, users=dict_users, action=action))
	else:
		##Get the user based on the username in the URL
		u = User(username=username)
		form = Chat_Form(message='')
		if (form.check(request)):
			form.send_message(user.id_user, u.id_user)
			return (redirect(url_for('chat', action='chat', username=username)))

		user.get_messages(u.id_user)
		user = user.data_to_dict('chat')
		u = u.data_to_dict('chat')
		for message in user['messages']:
			if (message['id_user_from'] == user['id_user']):
				message['user_from'] = user['username']
			else:
				message['user_to'] = u['username']
			print("Message : " + str(message))
		return (render_template('chat.html', title="Chat", user=user, u=u, action=action, form=form))