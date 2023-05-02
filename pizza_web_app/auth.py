from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from pizza_web_app import bcrypt
from db_read import get_user_id, get_user_info

auth_bp = Blueprint('auth',__name__, template_folder='templates/auth')

authentication_error = 'incorrect user name or password, please try again'

@auth_bp.route('/login', methods=["GET","POST"])
def log_in():
    if request.method == "POST":
        #form filled and sent, go do the work
        data = request.form
        user_name = data.get('email')
        password = data.get('password')
        user_id = get_user_id(user_name)
        if not user_id:
            #user does not exist
            flash(authentication_error,category='warning')
            return(render_template("log_in.html"))
        user_info = get_user_info(user_id)
        stored_password = user_info.password_hash
        password_check = bcrypt.check_password_hash(stored_password,password)
        if password_check == True:
            pass
            #email and password has matched, log user in
            #give user_id session token(s)
            #redirect to pizza page? 
        else:
            flash(authentication_error,category='warning')
            return redirect(url_for('auth.log_in'))
    elif request.method == 'GET':
        #page hit, display log in form
        return(render_template("log_in.html"))
