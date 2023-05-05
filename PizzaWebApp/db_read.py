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
    cstr = db_connection_string
    conn = pyodbc.connect(cstr)
    return(conn)

def basket_count(order_id): 
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT CASE WHEN COUNT(*) IS NULL THEN 0 ELSE COUNT(*) END AS pizza_count
    FROM [order].[pizzas] AS op
    WHERE op.order_id = ?""",order_id)
    basket_count = cursor.fetchone()
    conn.close()
    return basket_count.pizza_count

def check_open_orders(user_id): 
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT order_id FROM [order].[details] WHERE customer_id = ? AND status_id = 1",user_id)
    order_id = cursor.fetchone()
    conn.close()
    if order_id:
        return order_id.order_id
    else:
        return

def get_pizza_toppings():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT topping_id,topping_name,topping_category,cost FROM pizza.toppings")
    topping_info = cursor.fetchall()
    conn.close()
    return topping_info

def get_order_statuses():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status_id FROM [order].[status]")
    status_info = cursor.fetchall()
    conn.close()
    return status_info

def get_pizza_sizes():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT size_id,external_name,inches,cm,cost FROM pizza.sizes")
    size_id = cursor.fetchall()
    conn.close()
    return size_id

def get_user_id(user_name):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id FROM customer.details WHERE email = ?",user_name)
    user_id = cursor.fetchone()
    conn.close()
    if user_id:
        return user_id.customer_id

def get_user_info(user_id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT customer_id, email, full_name, password_hash FROM customer.details WHERE customer_id = ?",user_id)
    user = cursor.fetchone()
    conn.close()
    return user

def get_basket(user_id, order_id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"EXEC [order].[basket] {order_id},{user_id}")
    basket = cursor.fetchone()
    conn.close()
    return basket

def get_basket_items(user_id, order_id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(f"EXEC [order].[basket_items] {order_id},{user_id}")
    basket_items = cursor.fetchall()
    conn.close()
    return basket_items