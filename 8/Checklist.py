import time
import sys
import sqlite3

database = "Checklist.db"
table = "Lists"


def addtoList(table,item):
    find_item = ("SELECT * FROM Lists WHERE item = ?")
    cursor.execute(find_item,[(item)])
    results = cursor.fetchall()
    if results:
        print("")
        print("[X] Item already in checklist")
        sys.exit()
    else:
        print("")
        print(f"[i] Adding {item} to the {database}...")
        cursor.execute(f"""
        INSERT INTO {table}(item)
        VALUES("{item}")
        """)
        db.commit()
        print("")
        print("[i] Verifying...")
        time.sleep(2)
        find_item = ("SELECT * FROM Lists WHERE item = ?")
        cursor.execute(find_item,[(item)])
        results = cursor.fetchall()
        if results:
            print("")
            print("[+] Item was added")
            sys.exit()
        else:
            print("")
            print(f"[X] An error occured adding {item} to {table} in the {database}")
            sys.exit()

#def removefromList():

def viewList():
    view_items = ("SELECT * FROM Lists")
    cursor.execute(view_items)
    results = cursor.fetchall()
    if results:
        print("")
        print("- Current Items -")
        for item in results:
            print(f"{item[0]} - {item[1]}")
        


def startScreen():
    try:
        print("")
        print("<-- Check List -->")
        options = int(input("1) Add a new Item\n2) Remove a Item\n3) View current Items\nOption: "))
        return options
    except KeyboardInterrupt:
        print("")
        print("[X] Closing....")
        sys.exit()

while True:
    try:
        option = startScreen()
        with sqlite3.connect(database) as db:
            cursor = db.cursor()

        if option == 1:
            print("")
            item = input("What would you like to add to the list?\nItem: ")
            addtoList(table,item)
        elif option == 2:
            #removefromList()
            continue
        elif option == 3:
            viewList()
        else:
            print("")
            print("[X] Invalid Option")

    except KeyboardInterrupt:
        print("")
        print("[X] Closing....")
        sys.exit()
    

