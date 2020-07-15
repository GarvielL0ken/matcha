#imports
##Standard Library
##Third Party
from flask import redirect, render_template, request, session, url_for

##Local
from app import app
from app.forms.edit_profile_form import Edit_Profile_Form
from app.models import User

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	##Redirect if not logged in
	try:
		if (session['id_user'] != 0):
			user = User(session['id_user'])
	except:
		return redirect(url_for('login'))
	action = request.args.get('action')
	user = User(session['id_user'])
	form = 0

	##if (user.data_incomplete):
	##	action = 'edit
	if (not user.gender):
		action = 'edit'
	if (action == 'edit'):
		form = Edit_Profile_Form(gender = user.gender)
		if (form.check(request)):
			form.update_user_data(request, user)
	u = user.data_to_dict('profile')
	return (render_template('profile.html', title="Profile", user=u, form=form, action=action))