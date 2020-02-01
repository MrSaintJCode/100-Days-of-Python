import time
import sys
import sqlite3

# DB = users.db
# Table = users
# -- Table Info --
# userID
# username
# password
# FirstName
# LastName

database = "users.db"

def LoginSuccess(username):
    print("")
    print(f"<-- Welcome {username} -->")
    return True

def login():
    tries = 5
    while tries > 0:
        try:
            print("")
            print("--> Login System <--")
            username = input("Username: ")
            password = input("Password: ")
            with sqlite3.connect(database) as db:
                cursor = db.cursor()

            find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")

            cursor.execute(find_user,[(username),(password)])
            results = cursor.fetchall()

            if results:
                LoginSuccess(username)
                #return("exit")
            else:
                print("")
                print("[X] Username or Password Invalid")
                tries = tries - 1

        except KeyboardInterrupt:
            print("")
            print("[X] Closing...")
            sys.exit()

login()