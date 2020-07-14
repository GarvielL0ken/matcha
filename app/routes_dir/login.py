#imports
##Standard Library
##Third Party
from flask import redirect, render_template, request, url_for
from app.forms.login_form import Login_Form

##Local
from app import app

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = Login_Form()
	if (request.method == 'POST'):
		if (form.check()):
			form.login()
			return redirect(url_for('profile'))
	return (render_template('login.html', title="Login", form=form))