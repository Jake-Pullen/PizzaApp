from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from db_read import get_pizza_sizes, get_pizza_toppings
from db_write import new_custom_pizza

order_bp = Blueprint('order',__name__, template_folder='templates/order')

@order_bp.route('/', methods=["GET","POST"])
def pizza_maker():
    #check user is logged in, if not send them to log in
    user_id = session.get('user_id')
    if not user_id:
        flash('please log in first', category='danger')
        return redirect(url_for('auth.log_in'))
    if request.method == "GET":
        toppings = get_pizza_toppings()
        sizes = get_pizza_sizes()
        return render_template('order_pizza.html',
                               toppings=toppings,
                               sizes=sizes,
                               user_id = user_id)
    elif request.method == "POST":
        order_details = request.form
        new_custom_pizza(order_details)