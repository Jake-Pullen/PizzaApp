import pyodbc
import socket

def sql_ver(host_name):
    if host_name == 'Work-JP': #because JP is stupid enough to have 2 sql engines.... 
        return '\MSSQLSERVER22'
    else:
        return ''
host_name = socket.gethostname()
sql_version = sql_ver(host_name)

server = f'{host_name}{sql_version}'
database = 'pizza_master' #probably? maybe 'pizzaDB'
db_connection_string = fr'Driver=SQL Server;Server={server};Database={database};Trusted_Connection=yes;'


def connection():
    cstr = db_connection_string#.value
    conn = pyodbc.connect(cstr)
    return(conn)

def get_pizza_toppings():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT topping_id,topping_name,topping_category,cost FROM pizza.toppings")
    topping_info = cursor.fetchall()
    conn.close()
    return topping_info

def get_pizza_sizes():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT TOP(1) size_id FROM pizza.sizes")
    size_id = cursor.fetchall()
    conn.close()
    return size_id

def get_user_id(user_name):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id FROM customer.details WHERE email = ?",user_name)
    user_id = cursor.fetchone()
    conn.close()
    return user_id

def get_user_info(user_id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id, email, full_name, password_hash FROM customer.details WHERE customer_id = ?",user_id)
    user = cursor.fetchone()
    conn.close()
    return user
