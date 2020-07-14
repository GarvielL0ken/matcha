#imports
##Standard Library
##Third Party
from flask import redirect, session, url_for

##Local
from app import app

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	session['id_user'] = 0
	return (redirect(url_for('login')))