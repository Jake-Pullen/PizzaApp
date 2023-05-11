import os 
from waitress import serve
from pizza_web_app import app 

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT','5555'))
    except ValueError:
        PORT = 5555
    if HOST == 'localhost':
        app.run(HOST,PORT,debug=True)
    else:
        serve(app,host=HOST,port=PORT,threads=1)