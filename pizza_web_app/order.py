from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from db_read import get_pizza_sizes, get_pizza_toppings
from db_write import new_custom_pizza

order_bp = Blueprint('order',__name__, template_folder='templates/order')

@order_bp.route('/', methods=["GET","POST"])
def pizza_maker():
    pass
    #check user is logged in, if not send them to log in
