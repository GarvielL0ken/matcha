#imports
##Standard Library
##Third Party
from flask import render_template

##Local
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title="Home")