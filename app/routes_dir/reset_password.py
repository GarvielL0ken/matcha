#imports
##Standard Library
##Third Party
from flask import flash, redirect, render_template, request, session, url_for

##Local
from app import app
from app.forms.reset_forms import Reset_Password_Email_Form, Reset_Password_Form

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
	action = request.args.get('action')

	if (action == 'email'):
		form = Reset_Password_Email_Form()
	if (action == 'change_password'):
		form = Reset_Password_Form()

	if (form.check(request)):
		form.action(action, request)
	flash('hash {}, submit {}'.format(request.args.get('hash'), form.submit))
	return (render_template('reset_password.html', title="Reset Password", form=form))