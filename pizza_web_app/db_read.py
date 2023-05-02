import pyodbc

db_connection_string = 'a_string_here'

def connection():
    cstr = db_connection_string.value
    conn = pyodbc.connect(cstr)
    return(conn)

class db_user:
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
        cursor.execute("SELECT * FROM customer.details WHERE email = ?",user_id)# i know * bad practice, fight me
        user = cursor.fetchone()
        conn.close()
        return user
