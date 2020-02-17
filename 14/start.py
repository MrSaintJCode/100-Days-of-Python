import requests
import os
from appscript import app, mactypes
from datetime import datetime
import sqlite3
import shutil

##################################################
# Thanks to reddit users - enricojr and JunkyByte
##################################################

wallpaper_txt = "current_wallpaper.txt"

url = "https://source.unsplash.com/random/2560x1600"
export_name = f"Desktop_{datetime.now()}.jpeg"

def grab_new(url, export_name):
    print("")
    print("* Fetching new wallpaper from the web")
    r = requests.get(url)
    with open(export_name, 'wb') as image:
        image.write(r.content)

def set_new(export_name,wallpaper_txt):
    
    new_wallpaper = open(wallpaper_txt, "w+")

    new_wallpaper.write(export_name)
    app('Finder').desktop_picture.set(mactypes.File(export_name))
    print("")
    return print("* New wallpaper has been set")
    

def clean_old(wallpaper_txt):
    current_wallpaper = open(wallpaper_txt, "r")
    wallpaper = current_wallpaper.readline()
    os.remove(wallpaper)
    os.remove(wallpaper_txt)
    if os.path.isfile(wallpaper_txt):
        print("")
        return print("* Error removing current wallpaper")
    else:
        print("")
        return print("* Old wallpaper removed")

def save_desktop(wallpaper_txt):
    current_wallpaper = open(wallpaper_txt, "r")
    wallpaper = current_wallpaper.readline()

    ######## CREATING DATABASE AND TABLE ############
    database = "database/saved.db"
    table = "Images"
    table_content = ["imageID","imageName"]

    new_table = f"""
        CREATE TABLE IF NOT EXISTS {table}(
            {table_content[0]} INTEGER PRIMARY KEY,
            {table_content[1]} VARCHAR(20) NOT NULL
        )
    """

    with sqlite3.connect(database) as db:
        cursor = db.cursor()

    cursor.execute(new_table)
    ######## CREATING DATABASE AND TABLE ############

    with sqlite3.connect(database) as db:
        cursor = db.cursor()

    find_image = (f"SELECT * FROM Images WHERE imageName = ?")
    cursor.execute(find_image,[(wallpaper)])
    results = cursor.fetchall()

    if results:
        print("")
        return print("* Image was already saved")
    else:
        print("")
        print("* Saving image to the database")
        cursor.execute(f"""
            INSERT INTO Images(imageName)
            VALUES("{wallpaper}")
        """)
        db.commit()
        find_image = (f"SELECT * FROM Images WHERE imageName = ?")
        cursor.execute(find_image,[(wallpaper)])
        results = cursor.fetchall()
        if results:
            ######## COPYING CURRENT WALLPAPER ########
            savedFile = "database/images/"
            shutil.copy(wallpaper, savedFile)
            print("")
            return print("* Image has been saved to the db")
            ######## COPYING CURRENT WALLPAPER ########
        else:
            print("")
            return print("* Couldn't add image to the db")

def view_saved(wallpaper_txt):
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
        
            user_input = int(input("imageID - "))
            find_image = (f"SELECT * FROM Images WHERE imageID = ?")
            cursor.execute(find_image,[(user_input)])
            results = cursor.fetchall()
            if results:
                imageTable= ("SELECT * FROM Images WHERE imageID = ?")
                cursor.execute(imageTable,[(user_input)])
                results = cursor.fetchall()
                for image in results:
                    image_name = image[1]


                print("")
                print(f"* {user_input} exist, changing wallpaper ")
                clean_old(wallpaper_txt)
                saved_file = f"database/images/{image_name}"
                shutil.copy(saved_file, ".")
                set_new(image_name,wallpaper_txt)
                break

            else:
                print("")
                print(f"{userInput} is not valid")

def delete_saved():
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

if __name__ == '__main__':
    try:
        try:
            print("")
            print("---> CONTROL-C TO EXIT <---")
            userInput = int(input("What would you like to do:\n1) New Wallpaper\n2) Save Current Wallpaper\n3) View Saved Wallpapers\n4) Delete a Saved Wallpaper\nOption: "))
            if userInput == 1:
                if os.path.isfile(wallpaper_txt):
                    print("")
                    print("* Removing pervious wallpaper")
                    clean_old(wallpaper_txt)
                    grab_new(url,export_name)
                    set_new(export_name,wallpaper_txt)
                else:
                    grab_new(url,export_name)
                    set_new(export_name,wallpaper_txt)
            elif userInput == 2:
                save_desktop(wallpaper_txt)
            elif userInput == 3:
                view_saved(wallpaper_txt)
            elif userInput == 4:
                delete_saved()
            else:
                print("")
                print("* Input invalid")
        except KeyboardInterrupt:
            print("")
            print("Bye! :)")
    except (ValueError,OSError) as reason:
        print("")
        print("---- The following error occured ----")
        print(reason)