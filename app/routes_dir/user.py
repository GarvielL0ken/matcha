#imports
##Standard Library
##Third Party
from flask import redirect, render_template, request, session, url_for

##Local
from app import app
from app.forms.user_actions import User_Actions_Form
from app.models import User

@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
	##Redirect if not logged in
	try:
		if (session['id_user'] != 0):
			user = User(session['id_user'])
	except:
		return redirect(url_for('login'))

	u = User(username=username)
	user.view_user(u.id_user)
	
	form = User_Actions_Form()
	form.check(user, u)

	u.determine_like_status(user.id_user)
	viewed_user = u.data_to_dict('view')
	return (render_template('user.html', user=viewed_user, form=form))