import pyodbc
import socket

def sql_ver(host_name):
    if host_name == 'Work-JP': #because JP is stupid enough to have 2 sql engines.... 
        return 'MSSQLSERVER22'
    else:
        return 'MSSQLSERVER'
host_name = socket.gethostname()
sql_version = sql_ver(host_name)

server = f'{host_name}\{sql_version}'
database = 'pizza_master' #probably? maybe 'pizzaDB'
db_connection_string = fr'Driver=SQL Server;Server={server};Database={database};Trusted_Connection=yes;'

    

def connection():
    cstr = db_connection_string
    conn = pyodbc.connect(cstr)
    return(conn)

def populate_toppings():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO pizza.toppings 
VALUES 
 ('Pepperoni','Meat',2.5)
,('Sausage','Meat',2.5)
,('Ham','Meat',2.5)
,('Bacon','Meat',2.5)
,('Chicken','Meat',2.5)
,('Ground beef','Meat',2.5)
,('Shrimp','Meat',2.5)
,('Anchovies','Meat',2.5)
,('Mushrooms','Vegetables',2)
,('Onions','Vegetables',2)
,('Bell peppers','Vegetables',2)
,('Green peppers','Vegetables',2)
,('Red peppers','Vegetables',2)
,('Jalepenios','Vegetables',2)
,('Gerkhins','Vegetables',2)
,('Black olives','Vegetables',2)
,('Green olives','Vegetables',2)
,('Artichoke hearts','Vegetables',2)
,('Spinach','Vegetables',2)
,('Zucchini','Vegetables',2)
,('Eggplant','Vegetables',2)
,('Pineapple','Vegetables',2)
,('chilli flakes','misc',1.5)
,('burger sauce','misc',1.5)
,('Mozzarella','Cheese',1)
,('Parmesan','Cheese',1)
,('Romano','Cheese',1)
,('Fontina','Cheese',1)
,('Gruyère','Cheese',1)
,('Gorgonzola','Cheese',1)
,('Blue cheese','Cheese',1)
,('Goat cheese','Cheese',1);""")
    conn.commit()
    conn.close()
    return

def populate_sizes():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO pizza.sizes
VALUES 
 (1,'Small',6,15,7)
,(2,'Medium',9,23,12)
,(3,'Large',12,30,16)
,(4,'MEGA',15,38,20);""")
    conn.commit()
    conn.close()
    return

def add_new_customer(data,pw_hash):
    email = data.get('email')
    full_name = data.get('full_name')
    phone_num = data.get('phone_num')
    street_address = data.get('street_address')
    city = data.get('city')
    postcode = data.get('postcode')
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO customer.details
    VALUES(?,?,?,?,?,?,?)
    """,email,full_name,phone_num,street_address,city,postcode,pw_hash
    )
    conn.commit()
    conn.close()
    return