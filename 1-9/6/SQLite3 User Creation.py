import sqlite3
import os.path
import time
import sys

dbName = "users"
table = "user"

with sqlite3.connect(f"{dbName}.db") as db:
    cursor = db.cursor()


while True:
    try:
        print("")
        print("<---- New User ---->")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        username = input("Username: ")
        password = input("Password: ")
    except KeyboardInterrupt:
        print("")
        print("[X] Closing...")
        sys.exit()

    
    

    cursor.execute(f"""
    INSERT INTO {table}(username,password,FirstName,LastName)
    VALUES("{username}","{password}","{first_name}","{last_name}")
    """)
    db.commit()
    


