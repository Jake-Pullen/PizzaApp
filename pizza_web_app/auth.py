from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from pizza_web_app import bcrypt
from db_read import get_user_id, get_user_info
from db_write import add_new_customer

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
            return(render_template("testing.html"))
        else:
            flash(authentication_error,category='warning')
            return redirect(url_for('auth.log_in'))
    elif request.method == 'GET':
        #page hit, display log in form
        return(render_template("log_in.html"))

@auth_bp.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        #form filled and sent, go do the work
        data = request.form
        email = data.get('email')
        password1 = data.get('password')
        password2 = data.get('password2')
        #first check user doesnt already exist
        account = get_user_id(email)
        if account:
            flash('you already have an account',category='danger')
            return redirect(url_for('auth.log_in'))
        #then make sure password entry is correct
        elif password1 != password2:
            flash('learn to type your passwords correctly please', category='danger')
        else:
            #lets secure this password
            pw_hash = bcrypt.generate_password_hash(password1).decode('utf-8')
            #add the details to the db
            add_new_customer(data,pw_hash)
            #send them to the log in page
            return redirect(url_for('auth.log_in'))
    elif request.method == 'GET':
        #page hit, display log in form
        return(render_template("register.html"))