import csv
import random

from db.connect import connect_db
def create_name():
    with open('data/name_data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    random_row = random.choice(data)
    return random_row[0]

def create_adjectives():
    with open('data/adjectives.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    random_row = random.choice(data)
    return random_row[0]

def create_username():
    while(True):
        first_adjectives = create_adjectives()
        second_name = create_name()
        username = first_adjectives + " " + second_name
        username = "testname"
        if overlap_username_chk(username):
           continue
        else:
            return insert_username(username)
        
def overlap_username_chk(username):
    conn = connect_db()
    cursor = conn.cursor()
    query = cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
    result = query.fetchone()
    return result

def insert_username(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username) VALUES(?)", (username,))
    conn.commit()
    return username
