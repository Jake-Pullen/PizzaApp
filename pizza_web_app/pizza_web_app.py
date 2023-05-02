from flask import Flask 
from flask_bcrypt import Bcrypt
from db_read import check_sizes,check_toppings
from db_write import populate_toppings,populate_sizes

secret_key = 'this_is_not_a_secure_secret_key'

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = secret_key #.value #used for when we set a proper secret key


from auth import auth_bp
from home import home_bp
#from order import order_bp

app.register_blueprint(auth_bp,url_prefix='/authentication')
app.register_blueprint(home_bp)
#app.register_blueprint(order_bp,url_prefix='/new_order')

is_toppings = check_toppings()
is_sizes = check_sizes() 

if not is_toppings: 
    populate_toppings()
if not is_sizes:
    populate_sizes() 

print('Web Server Active on localhost:5555')