#imports

##Standard Library

##Third Party
from flask import redirect, render_template, request, url_for

##Local
from app import app
from app.forms.registration_form import Registration_Form

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = Registration_Form()
	if (request.method == 'POST'):
		if (form.check()):
			form.add_user()
			return redirect(url_for('login'))
	#if (form.check(data)):
	#	flash('username {}, submit {}'.format(form.username.data, form.submit))
	return (render_template('register.html', title="Register", form=form))