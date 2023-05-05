from flask import Blueprint, render_template, request, flash, redirect, url_for, session, Markup
from db_read import get_pizza_sizes, get_pizza_toppings,check_open_orders
from db_write import new_custom_pizza, start_new_order

order_bp = Blueprint('order',__name__, template_folder='templates/order')
pizza_count = int(0)

@order_bp.route('/', methods=["GET"])
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
    
@order_bp.route('/add_to_basket', methods=["POST"])
def add_to_basket():
    '''
    when user logs in, we should check for open orders and place cookie.
    when pizza placed in basket
    if cookie order_id = 0:
        generate order number & update cookie
    place order_id & size_id into order.pizza and generate new order_pizza_id
    get order_pizza_id and place in order.pizza_toppings along with topping id (1 per topping)
    '''
    user_id = session.get('user_id')
    order_id = session.get('order_id')
    if order_id == 0:
        start_new_order(user_id)
        order_id = check_open_orders(user_id)
        session['order_id'] = order_id
    order_details = request.form
    pizza_size = order_details.get('selected_size')
    pizza_toppings = order_details.getlist('selected_topping')
    print(user_id, order_id, pizza_size, pizza_toppings)
    new_custom_pizza(order_id, order_details)
    flash(Markup('Added to basket, <a href="'+ url_for('order.view_basket') +'">View basket</a> or continue adding pizza.'), category='success')
    return redirect(url_for('order.pizza_maker'))


@order_bp.route('/basket', methods=["GET","POST"])
def view_basket():
    if request.method == "GET":        
        user_id = session.get('user_id')
        order_id = session.get('order_id')
        print(user_id,order_id)
        return render_template('view_basket.html')



