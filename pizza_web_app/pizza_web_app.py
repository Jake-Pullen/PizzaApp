from flask import Flask 
from flask_bcrypt import Bcrypt

secret_key = 'this_is_not_a_secure_secret_key'

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = secret_key #.value #used for when we set a proper secret key


from auth import auth_bp
from home import home_bp

app.register_blueprint(auth_bp,url_prefix='/authentication')
app.register_blueprint(home_bp)

print('Web Server Active on localhost:5555')