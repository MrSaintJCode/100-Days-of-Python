import sqlite3
import os.path
import time

dbName = "users"
table = "user"

with sqlite3.connect(f"{dbName}.db") as db:
    cursor = db.cursor()


while True:
    print("")
    print("<---- New User ---->")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    password = input("Password: ")
    
    

    cursor.execute(f"""
    INSERT INTO {table}(username,password,first_name,last_name)
    VALUES("{username}","{password}","{first_name}","{last_name}")
    """)
    db.commit()
    


