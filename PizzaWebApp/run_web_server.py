import os 
from waitress import serve
from pizza_web_app import app 

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    if HOST == 'localhost':
        PORT = 5555
        app.run(HOST,PORT,debug=True)
    else:
        PORT = 80
        serve(app,host=HOST,port=PORT,threads=1)