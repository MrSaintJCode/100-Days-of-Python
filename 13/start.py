import requests
import os.path
import os
import sys, time
from appscript import app, mactypes
from datetime import datetime
import sqlite3
import shutil

wallpaper_txt = "current_wallpaper.txt"

url = "https://source.unsplash.com/random/2560x1600"
export_name = f"Desktop_{datetime.now()}.jpeg"

def grabNew(url, export_name):
    print("")
    print("* Fetching new wallpaper from the web")
    r = requests.get(url)
    with open(export_name, 'wb') as image:
        image.write(r.content)

def setNew(export_name,wallpaper_txt):
    
    new_wallpaper = open(wallpaper_txt, "w+")

    if os.path.isfile(wallpaper_txt):
        new_wallpaper.write(export_name)
        time.sleep(2)
        app('Finder').desktop_picture.set(mactypes.File(export_name))
        sys.exit()
    else:
        print("")
        print("* An error occured in setNew function")
        sys.exit()

def cleanOld(wallpaper_txt):
    current_wallpaper = open(wallpaper_txt, "r")
    wallpaper = current_wallpaper.readline()
    os.remove(wallpaper)
    time.sleep(1)
    os.remove(wallpaper_txt)
    if os.path.isfile(wallpaper_txt):
        print("")
        print("* Error removing current wallpaper")
        sys.exit()
    else:
        print("")
        print("* Old wallpaper removed")

def saveDesktop(wallpaper_txt):
    current_wallpaper = open(wallpaper_txt, "r")
    wallpaper = current_wallpaper.readline()

    ######## CREATING DATABASE AND TABLE ############
    database = "database/saved.db"
    table = "Images"
    tableContent = ["imageID","imageName"]

    newTable = f"""
        CREATE TABLE IF NOT EXISTS {table}(
            {tableContent[0]} INTEGER PRIMARY KEY,
            {tableContent[1]} VARCHAR(20) NOT NULL
        )
    """

    with sqlite3.connect(database) as db:
        cursor = db.cursor()

    cursor.execute(newTable)
    ######## CREATING DATABASE AND TABLE ############


    if os.path.isfile(database):


        with sqlite3.connect(database) as db:
            cursor = db.cursor()

        find_image = (f"SELECT * FROM Images WHERE imageName = ?")
        cursor.execute(find_image,[(wallpaper)])
        results = cursor.fetchall()

        if results:
            print("")
            print("* Image was already saved")
            sys.exit()
        else:
            print("")
            print("* Saving image to the database")
            cursor.execute(f"""
                INSERT INTO Images(imageName)
                VALUES("{wallpaper}")
            """)
            db.commit()
            time.sleep(1)
            find_image = (f"SELECT * FROM Images WHERE imageName = ?")
            cursor.execute(find_image,[(wallpaper)])
            results = cursor.fetchall()
            if results:
                print("")
                print("* Image has been saved to the db")
                ######## COPYING CURRENT WALLPAPER ########
                savedFile = "database/images/"
                shutil.copy(wallpaper, savedFile)
                sys.exit()
                ######## COPYING CURRENT WALLPAPER ########

            else:
                print("")
                print("* Couldn't add image to the db")
                sys.exit()



    else:
        print("")
        print(f"* Couldn't create {database}")
        sys.exit()

def viewSaved(wallpaper_txt):
    database = "database/saved.db"

    with sqlite3.connect(database) as db:
        cursor = db.cursor()

    view_item = ("SELECT * FROM Images")
    cursor.execute(view_item)
    results = cursor.fetchall()
    if results:
        print("######################################################")
        print("#            ->  Saved Wallpapers  <-                #")
        print("#imageID  -  imageName                               #")
        print("######################################################")
        while True:
            for image in results:
                print(f"{image[0]} - {image[1]}")
        
            userInput = int(input("imageID - "))
            find_image = (f"SELECT * FROM Images WHERE imageID = ?")
            cursor.execute(find_image,[(userInput)])
            results = cursor.fetchall()
            if results:
                imageTable= ("SELECT * FROM Images WHERE imageID = ?")
                cursor.execute(imageTable,[(userInput)])
                results = cursor.fetchall()
                for image in results:
                    global imageName
                    imageName = image[1]


                print("")
                print(f"* {userInput} exist, changing wallpaper ")
                cleanOld(wallpaper_txt)
                time.sleep(1)
                savedFile = f"database/images/{imageName}"
                shutil.copy(savedFile, ".")
                time.sleep(1)
                setNew(imageName,wallpaper_txt)
                break

            else:
                print("")
                print(f"{userInput} is not valid")

def deleteSaved():
    database = "database/saved.db"

    with sqlite3.connect(database) as db:
        cursor = db.cursor()

    view_item = ("SELECT * FROM Images")
    cursor.execute(view_item)
    results = cursor.fetchall()
    if results:
        print("######################################################")
        print("#            ->  Saved Wallpapers  <-                #")
        print("#imageID  -  imageName                               #")
        print("######################################################")
        while True:
            for image in results:
                print(f"{image[0]} - {image[1]}")
        
            userInput = int(input("imageID - "))
            find_image = (f"SELECT * FROM Images WHERE imageID = ?")
            cursor.execute(find_image,[(userInput)])
            results = cursor.fetchall()
            if results:
                print("")
                delete_query = """DELETE from Images where imageID = ?"""
                cursor.execute(delete_query,[(image[0])])
                db.commit()
                if os.path.isfile(f"database/images/{image[1]}"):
                    os.remove(f"database/images/{image[1]}")
                    if os.path.isfile(f"database/images/{image[1]}"):
                        print("")
                        print(f"* Couldn't remove {image[1]} from the saved folder")
                        
                print("")
                print(f"* {image[1]} has been deleted")
                break

try:
    while True:
        try:
            print("")
            print("---> CONTROL-C TO EXIT <---")
            userInput = int(input("What would you like to do:\n1) New Wallpaper\n2) Save Current Wallpaper\n3) View Saved Wallpapers\n4) Delete a Saved Wallpaper\nOption: "))

            if userInput == 1:
                if os.path.isfile(wallpaper_txt):
                    print("")
                    print("* Removing pervious wallpaper")
                    cleanOld(wallpaper_txt)
                    time.sleep(1)
                    grabNew(url,export_name)
                    time.sleep(1)
                    setNew(export_name,wallpaper_txt)
                else:
                    grabNew(url,export_name)
                    time.sleep(1)
                    setNew(export_name,wallpaper_txt)
            elif userInput == 2:
                saveDesktop(wallpaper_txt)
            elif userInput == 3:
                viewSaved(wallpaper_txt)
            elif userInput == 4:
                deleteSaved()
            else:
                print("")
                print("* Input invalid")
        except KeyboardInterrupt:
            print("")
            print("Bye! :)")
            sys.exit()
            

except (ValueError) as reason:
    print("")
    print(f"* Session closed because of {reason}")
