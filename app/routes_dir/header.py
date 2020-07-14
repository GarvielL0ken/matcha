from flask import render_template, flash, redirect, request, session, url_for
from app import app
from app.forms import Registration_Form, Login_Form, Reset_Password_Email_Form, Reset_Password_Form, User_Data_Form, User_Actions_Form
from app.models import User
import array
from app.sql.functions import is_in_database