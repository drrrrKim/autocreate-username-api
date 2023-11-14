import sqlite3

def connect_db():
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    return conn





