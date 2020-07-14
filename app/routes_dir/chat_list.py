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
	if (session['id_user'] == 0):
		return redirect(url_for('login'))

	lst_users = []
	u = User(1)
	u.set_message('I like apples', '2 min ago')
	lst_users.append((u.data_to_dict('chat_preview')))
	u = User(2)
	u.set_message("I don't like apples", 'now')
	lst_users.append(u.data_to_dict('chat_preview'))
	return (render_template('chat.html', title="Chat", users=lst_users))