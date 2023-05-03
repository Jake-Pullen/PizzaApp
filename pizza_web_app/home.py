#add home page here, link to log in and register 
from flask import Blueprint, render_template, request, flash, redirect, url_for, session

home_bp = Blueprint('home',__name__, template_folder='templates/home')

@home_bp.route('/')
def home_page():
    return render_template('home_page.html')

@home_bp.route('/clear_session')
def clear_session():
    session.clear()
    flash('All Clear!',category='success')
    return redirect(url_for('home.home_page'))
