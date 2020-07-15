#imports
##Standard Library
##Third Party
from flask import redirect, render_template, request, session, url_for

##Local
from app import app
from app.forms.user_actions import User_Actions_Form
from app.models import User

@app.route('/user/<username>')
def user(username):
	##Redirect if not logged in
	try:
		if (session['id_user'] != 0):
			user = User(session['id_user'])
	except:
		return redirect(url_for('login'))

	u = User(username)
	
	form = User_Actions_Form()
	if (form.check(request)):
		form.action(request, user.id_user, u.id_user)

	viewed_user = u.data_to_dict('view')
	return (render_template('user.html', user=viewed_user, form=form))