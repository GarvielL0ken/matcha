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
	if (session['id_user'] == 0):
		return redirect(url_for('login'))

	print(request)
	u = User(1)
	user = u.data_to_dict('view')
	form = User_Actions_Form()
	form.check()
	return (render_template('user.html', user=user, form=form))