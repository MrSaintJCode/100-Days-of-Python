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
        else:
            print("")
            print(f"[X] An error occured adding {item} to {table} in the {database}")
            sys.exit()

def removefromList(table,itemID):
    print("")
    find_itemID = ("SELECT * FROM Lists WHERE itemID = ?")
    cursor.execute(find_itemID,[(itemID)])
    results = cursor.fetchall()
    if results:
        for item in results:
            confirmation = input(f"Are you sure you'd like to remove {item[1]}? (Y/N)\nConfirmation: ")
            if confirmation.lower() == "y":
                print("")
                print(f"[i] Removing {item[1]}...")
                time.sleep(3)
                delete_query = """DELETE from Lists where itemID = ?"""
                cursor.execute(delete_query,[(itemID)])
                db.commit()
                print("")
                print("[i] Verifying...")
                find_itemID = ("SELECT * FROM Lists WHERE itemID = ?")
                cursor.execute(find_itemID,[(itemID)])
                results = cursor.fetchall()
                if results:
                    print("")
                    print(f"[X] An error occured deleting {item[1]} to {table} in the {database}")
                    sys.exit()
                else:
                    print("")
                    print("[+] Item was deleted")



            else:
                print("")
                print("[X] Deletion Canceled")
                sys.exit()
    else:
        print("")
        print("[X] Item doesn't exist")
        sys.exit()


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
        try:
            print("")
            print("<-- Check List -->")
            options = int(input("1) Add a new Item\n2) Remove a Item\n3) View current Items\nOption: "))
            return options
        except ValueError:
            print("")
    except KeyboardInterrupt:
        print("")
        print("[X] Closing....")
        sys.exit()

while True:
    try:
        print("")
        print("[i] CTRL-C to exit")
        option = startScreen()
        with sqlite3.connect(database) as db:
            cursor = db.cursor()

        if option == 1:
            print("")
            item = input("What would you like to add to the list?\nItem: ")
            addtoList(table,item)
        elif option == 2:
            print("")
            itemID = int(input("Which item would you like to remove?(Item ID)\nItem ID: "))
            removefromList(table, itemID)
        elif option == 3:
            viewList()
        else:
            print("")
            print("[X] Invalid Option")

    except KeyboardInterrupt:
        print("")
        print("[X] Closing....")
        sys.exit()
    

