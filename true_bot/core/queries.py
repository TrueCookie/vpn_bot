from datetime import datetime
from . import db

DB_NAME = 'vb'
DB_USER = 'postgres'
DB_PASS = 'root'
DB_ADDR = 'localhost'
DB_PORT = 5432

def add_client(client_id):
    conn = db.create_conn(DB_NAME, DB_USER, DB_PASS, DB_ADDR, DB_PORT)

    curr_date = datetime.now().strftime('%Y-%m-%d')
    db.execute_query(conn, 
                     f"""insert into client (client_id, sub_upd_date)
                        values ('{client_id}', '{curr_date}')""")

def upd_client_sub(client_id) -> tuple:
    conn = db.create_conn(DB_NAME, DB_USER, DB_PASS, DB_ADDR, DB_PORT)
    
    curr_date = datetime.now().strftime('%Y-%m-%d')
    db.execute_query(conn, 
                    f"""update client
                        set sub_upd_date = '{curr_date}'
                        where client_id = '{client_id}'""")

def get_client(client_id):
    conn = db.create_conn(DB_NAME, DB_USER, DB_PASS, DB_ADDR, DB_PORT)
    
    cursor = conn.cursor()
    clients = None
    try:
        cursor.execute(f"""select client_id, sub_upd_date
                        from client
                        where client_id = '{client_id}'""")
        clients = cursor.fetchone()

        return clients
    except Exception as e:
        print(f"The error '{e}' occurred")
    