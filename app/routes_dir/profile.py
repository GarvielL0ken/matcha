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
	print('GET LOGGED ON USER')
	##Redirect if not logged in
	user = get_logged_on_user()
	if (not user):
		return redirect(url_for('login'))

	action = request.args.get('action')
	print("SESSION ID USER : " + str(session['id_user']))
	print('')
	print('GET LIKES AND VIEWS')
	user.set_likes()
	user.set_views()
	print('LIKES AND VIEWS SET')
	#user.set_tags()
	form = 0

	##if (user.data_incomplete):
	##	action = 'edit
	if (not user.gender):
		action = 'edit'
	if (action == 'edit'):
		form = Edit_Profile_Form(gender = user.gender, preferences = user.preferences_int_to_array(), bio = user.bio)
		if (form.check(request)):
			form.update_user_data(request, user)
			return (redirect(url_for('profile')))
	u = user.data_to_dict('profile')
	return (render_template('profile.html', title="Profile", user=u, form=form, action=action))