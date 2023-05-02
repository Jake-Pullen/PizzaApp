from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from pizza_web_app import bcrypt
from db_read import db_user

auth_bp = Blueprint('auth',__name__, template_folder='templates/auth')

authentication_error = 'incorrect user name or password, please try again'

def check_user_exists(user_name):
    user_id = db_user.get_user_id(user_name)
    if user_id:
        flash(authentication_error,category='warning')
        return False#render_template(url_for(auth.login))
    else:
        return user_id

def check_password_match(user_name,password):
    user_id = check_user_exists(user_name)
    user_info = db_user.get_user_info(user_id)
    stored_password = user_info.password_hash
    password_check = bcrypt.check_password_hash(stored_password,password)
    if password_check == True:
        pass
        #email and password has matched, log user in
    else:
        flash(authentication_error,category='warning')
        return redirect(url_for('auth.log_in'))

@auth_bp.route('/login', methods=["GET","POST"])
def log_in():
    if request.method == "POST":
        #form filled and sent, go do the work
        pass
    elif request.method == 'GET':
        #page hit, display log in form
        return(render_template("log_in.html"))
