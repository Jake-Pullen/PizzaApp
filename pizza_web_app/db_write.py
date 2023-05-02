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
    cstr = db_connection_string#.value
    conn = pyodbc.connect(cstr)
    return(conn)

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