import requests
import os.path
import os
import sys, time
from appscript import app, mactypes
from datetime import datetime
import sqlite3

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

#new_wallpaper = open(wallpaper_txt, "w+")
try:
    userInput = int(input("What would you like to do:\n1) New Wallpaper\n2) Save Current Wallpaper\nOption: "))

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
            # Create New one
            print("")
    
except (ValueError,KeyboardInterrupt) as reason:
    print("")
    print(f"* Session closed because of {reason}")
