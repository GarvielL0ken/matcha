#imports
##Standard Library
##Third Party
from flask import redirect, render_template, request, session, url_for

##Local
from app import app
from app.forms.edit_profile_form import Edit_Profile_Form
from app.models import User
from app.routes_dir.functions import get_logged_on_user

@app.route('/profile', methods=['GET', 'POST'])
def profile():
	##Redirect if not logged in
	user = get_logged_on_user()
	if (not user):
		return redirect(url_for('login'))

	action = request.args.get('action')
	user = User(session['id_user'])
	form = 0

	##if (user.data_incomplete):
	##	action = 'edit
	if (not user.gender):
		action = 'edit'
	if (action == 'edit'):
		print("user.preferences : " + str(user.preferences_int_to_array()))
		form = Edit_Profile_Form(gender = user.gender, preferences = user.preferences_int_to_array(), bio = user.bio)
		if (form.check(request)):
			form.update_user_data(request, user)
			return (redirect(url_for('profile')))
	u = user.data_to_dict('profile')
	return (render_template('profile.html', title="Profile", user=u, form=form, action=action))