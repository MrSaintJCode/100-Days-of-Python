import sqlite3
import sys
import os.path

def createDatabase(database):
    while True:
        print("")
        userINP = input(f"Are you sure you'd like to create {database}(Y/N)\nAnswer: ")
        if userINP.lower() == "y":
            db = sqlite3.connect(f"{database}.db")
            if os.path.isfile(f"{database}.db"):
                print("[+] Database has been created successfully")
                sys.exit()
            else:
                print("[X] There was an error creating the database")
                sys.exit()
        elif userINP.lower() == "n":
            print("")
            print("[X] Database creation has been canceled!")
            sys.exit()
        else:
            print("")
            print("[X] Invalid Response - Please Try Again")

def createTable(database, table):
    if os.path.isfile(f"{dbName}.db"):
        print("")
        print("--- Enter the table content ---")
        print("Type done when completed or press CTRL-C to cancel")
        tableContent = []
        line = 5
        while line > 0:
            try:
                print("")
                newTableContent = input("Field Name:")
                if newTableContent.lower() == "done":
                    break
                else:
                    tableContent.append(newTableContent)
                    line = line - 1
                        
            except KeyboardInterrupt:
                print("")
                print("[X] Closing...")
                sys.exit()

        print("")
        print("[+] Creating Table")
        print(f"{tableContent[0]}\n{tableContent[1]}\n{tableContent[2]}\n{tableContent[3]}\n{tableContent[4]}")
        newTable = f"""
        CREATE TABLE IF NOT EXISTS user(
            {tableContent[0]} INTEGER PRIMARY KEY,
            {tableContent[1]} VARCHAR(20) NOT NULL,
            {tableContent[2]} VARCHAR(20) NOT NULL,
            {tableContent[3]} VARCHAR(20) NOT NULL,
            {tableContent[4]} VARCHAR(20) NOT NULL
        )
        """
        database = sqlite3.connect(f"{dbName}.db")
        db = database.cursor()
        db.execute(newTable)
        print("")
        print(f"[i] Table has been created in the {dbName} database")
        sys.exit()

    else:
        print("")
        print(f"[X] {dbName} was not found")
        sys.exit()


print("")
print("CTRL-C to exit program")
while True:
    print("")
    print("--> SQLite3 Database Creation Tool <--")
    try:
        try:
            options = int(input("What would you like to do:\n1) Create a new database\n2) Create a new table\nOption: "))
            if options == 1:
                print("")
                dbName = input("What would you like to call this database:\nDatabase Name: ")
                createDatabase(dbName)
            elif options == 2:
                print("")
                dbName = input("Which database would you like to add a table too:\nDatabase Name: ")
                print("")
                tbName = input("What you like to call this table:\n Table Name: ")
                createTable(dbName, tbName)
            else:
                print("")
                print("[X] Invalid Option - Please try again")
        except ValueError:
            print("")
            print("[X] Invalid Option - Please try again")
    except KeyboardInterrupt:
        print("")
        print("[X] Closing...")
        sys.exit()



#userTable = """
#CREATE TABLE IF NOT EXISTS user(
#    userID INTEGER PRIMARY KEY,
#    username VARCHAR(20) NOT NULL,
#    first_name VARCHAR(20) NOT NULL,
#    last_name VARCHAR(20) NOT NULL,
#    password VARCHAR(20) NOT NULL
#);
#"""

#cursor.execute(userTable)
