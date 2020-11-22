import tkinter as tk
import time,sys,datetime
import sqlite3
import os.path

global database

database = "Database/Authentication.db"

################################
# Authentication Table Set up
# Table - Users
#[+] Creating Table
#userID
#FirstName
#LastName
#Username
#Password
#Email
################################

print("")
print("------- BEHIND THE SCENES -------")

def register():
    global registerPAN
    
    # Export Info
    #global FirstNameInfo
    #global LastNameInfo
    #global UsernameInfo
    #global PasswordInfo
    #global ConfirmPasswordInfo
    #global EmailInfo

    # Create a new user
    def newUser():
        database = "Database/Authentication.db"
        # Grabbing User Info
        FirstNameInfo = FirstName.get()
        LastNameInfo = LastName.get()
        UsernameInfo = Username.get()
        PasswordInfo = Password.get() 
        ConfirmPasswordInfo = ConfirmPassword.get()
        EmailInfo = Email.get() 

        print(f"""
        ------------------------------------------
        First Name - {FirstNameInfo}
        Last Name - {LastNameInfo}
        Username - {UsernameInfo}
        Password - {PasswordInfo}
        Confirm Password - {ConfirmPasswordInfo}
        Email - {EmailInfo}
        ------------------------------------------
        """)
        with sqlite3.connect(database) as db:
            cursor = db.cursor()

        find_user = ("SELECT * FROM Users WHERE Username = ?")
        cursor.execute(find_user,[(UsernameInfo)])
        results = cursor.fetchall()
        if results:
            print("")
            print("* User already exist")
            userexistPAN = tk.Tk(className=" Error")

            userexistLBL = tk.Label(userexistPAN,text="User Already Exist")
            userexistBTN = tk.Button(userexistPAN,text="Ok", command=userexistPAN.destroy)
            userexistLBL.pack()
            userexistBTN.pack()
            userexistPAN.mainloop()
        else:
            # Create the user
            if PasswordInfo == ConfirmPasswordInfo:
                print("")
                print(f"* Creating user {UsernameInfo} in the {database}")
                cursor.execute(f"""
                INSERT INTO Users(FirstName,LastName,Username,Password,Email)
                VALUES("{FirstNameInfo}","{LastNameInfo}","{UsernameInfo}","{PasswordInfo}","{EmailInfo}")
                """)
                db.commit()

                # Checking if user has been added
                find_user = ("SELECT * FROM Users WHERE Username = ?")
                cursor.execute(find_user,[(UsernameInfo)])

                results = cursor.fetchall()
                if results:
                    def reset():
                        time.sleep(2)
                        useraddedPAN.destroy()
                        registerPAN.destroy()
                        mainFUN()

                    useraddedPAN = tk.Tk(className=" Successful")
                    useraddedLBL = tk.Label(useraddedPAN,text="User has been added")
                    useraddedBTN = tk.Button(useraddedPAN,text="Awesome!",command=reset)

                    useraddedLBL.pack()
                    useraddedBTN.pack()

                    useraddedPAN.mainloop()
                else:
                    # User didn't add? Shouldn't ever happen.. but, you never know right?
                    # I need to work on my naming conventions. whatisthis + error ...
                    useraddERR = tk.Tk(className=" Error")
                    useraddLBL = tk.Label(useraddERR,text=" An error occured")
                    useraddBTN = tk.Button(useraddERR, text="Ok", command=useraddERR.destroy)

                    useraddLBL.pack()
                    useraddBTN.pack()

                    useraddERR.mainloop()




            else:
                print("")
                print("* Password doesnt match")
                passwordERR = tk.Tk(className=" Error")
                passwordERRLBL = tk.Label(passwordERR,text="Password Doesn't Match")
                passwordERRBTN = tk.Button(passwordERR,text="Ok", command=passwordERR.destroy)

                passwordERRLBL.pack()
                passwordERRBTN.pack()
                passwordERR.mainloop()




        
    # Back to main
    def goBack():
        registerPAN.destroy()
        mainFUN()


    
    # Kill main window
    main.destroy()

    # Main Window
    registerPAN = tk.Tk(className=" Register a new user")
    registerPAN.resizable(False, False)

    # First Name
    FirstNameLBL = tk.Label(registerPAN, text="First Name")
    FirstName = tk.Entry(registerPAN)
    
    # Last Name
    LastNameLBL = tk.Label(registerPAN, text="Last Name")
    LastName = tk.Entry(registerPAN)
    
    # Username
    UsernameLBL = tk.Label(registerPAN, text="Username")
    Username = tk.Entry(registerPAN)
    
    # Password
    PasswordLBL = tk.Label(registerPAN, text="Password")
    Password = tk.Entry(registerPAN, show="*")
    
    # Confirm Password
    ConfirmPasswordLBL = tk.Label(registerPAN, text="Confirm Password")
    ConfirmPassword = tk.Entry(registerPAN, show="*")
    
    # Email
    EmailLBL = tk.Label(registerPAN, text="Email")
    Email = tk.Entry(registerPAN)
    
    # Action Button
    Submit = tk.Button(registerPAN,text="Submit", command=newUser,width="10")
    Back = tk.Button(registerPAN,text="Back",command=goBack,width="10")
    
    # For Spacing
    nothing1 = tk.Label(registerPAN,text=" ")
    nothing2 = tk.Label(registerPAN,text=" ")
    
    # Display 
    FirstNameLBL.grid(row="1",column="1")
    FirstName.grid(row="1",column="2")
    
    LastNameLBL.grid(row="2",column="1")
    LastName.grid(row="2",column="2")
    
    UsernameLBL.grid(row="3",column="1")
    Username.grid(row="3",column="2")
    
    PasswordLBL.grid(row="4",column="1")
    Password.grid(row="4",column="2")
    
    ConfirmPasswordLBL.grid(row="5",column="1")
    ConfirmPassword.grid(row="5",column="2")
    
    EmailLBL.grid(row="6",column="1")
    Email.grid(row="6",column="2")
    
    nothing1.grid(row="7",column="1")
    
    Back.grid(row="8",column="1")
    Submit.grid(row="8",column="2")
    
    nothing2.grid(row="9",column="1")

    registerPAN.mainloop()

def login():
    global loginPAN
    main.destroy()

    def goBack():
        loginPAN.destroy()
        mainFUN()

    def loginEXE():
        global loginPAN
        print("")
        print("* Checking if user exist")
        UsernameInfo = loginUsernameEntry.get()
        PasswordInfo = loginPasswordEntry.get()

        def loginSuccess():
            userexistPAN.destroy()


        with sqlite3.connect(database) as db:
            cursor = db.cursor()

        find_user = ("SELECT * FROM Users WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(UsernameInfo),(PasswordInfo)])
        results = cursor.fetchall()

        if results:
            print("")
            print(f"* {UsernameInfo} exist")
            time.sleep(2)
            userexistPAN = tk.Tk(className=" Successful")
            userexistLBL = tk.Label(userexistPAN,text="Login Successful")
            userexistBTN = tk.Button(userexistPAN,text="Woo!", command=userexistPAN.destroy)

            userexistLBL.pack()
            userexistBTN.pack()

            userexistPAN.mainloop()
        else:
            print("")
            print(f"* {UsernameInfo} doesnt exist")
            userexistPAN = tk.Tk(className=" Error")
            userexistLBL = tk.Label(userexistPAN,text="Username or Password Invalid")
            userexistBTN = tk.Button(userexistPAN,text="Ok",command=loginSuccess)

            userexistLBL.pack()
            userexistBTN.pack()

            userexistPAN.mainloop()

        
    loginPAN = tk.Tk(className=" Login")

    # Username
    loginUsernameLBL = tk.Label(loginPAN,text="Username")
    loginUsernameEntry = tk.Entry(loginPAN)

    # Password
    loginPasswordLBL = tk.Label(loginPAN,text="Password")
    loginPasswordEntry = tk.Entry(loginPAN,show="*")

    # Buttons
    loginBTN = tk.Button(loginPAN,text="Login",command=loginEXE,width="10")
    backBTN = tk.Button(loginPAN,text="Back",command=goBack, width="10")

    # Spacing
    nothing1 = tk.Label(loginPAN,text=" ")
    nothing2 = tk.Label(loginPAN,text=" ")

    # Grid
    loginUsernameLBL.grid(row="1",column="1")
    loginUsernameEntry.grid(row="1",column="2")
    
    loginPasswordLBL.grid(row="3",column="1")
    loginPasswordEntry.grid(row="3",column="2")

    nothing1.grid(row="2",column="1")
    backBTN.grid(row="5",column="1")
    loginBTN.grid(row="5",column="2")
    nothing2.grid(row="4",column="1")

    loginPAN.mainloop()






# def forgotpas():

def mainFUN():
    global main
    
    # Main Window
    main = tk.Tk(className=" Main Window")
    main.geometry("300x290")
    main.resizable(False, False)
    
    # Buttons
    loginBTN = tk.Button(main,text="Login",width="300",height="9",bg="#50c21f",command=login)
    registerBTN = tk.Button(main, text="Sign Up",width="300",height="9",bg="#e39d2d",command=register)

    loginBTN.pack()
    registerBTN.pack()

    main.mainloop()

def db_notfound():
    def createDB():
        database = "Database/Authentication.db"

        table = "Users"
        tableContent = ["userID","FirstName","LastName","Username","Password","Email"]

        newTable = f"""
        CREATE TABLE IF NOT EXISTS {table}(
            {tableContent[0]} INTEGER PRIMARY KEY,
            {tableContent[1]} VARCHAR(20) NOT NULL,
            {tableContent[2]} VARCHAR(20) NOT NULL,
            {tableContent[3]} VARCHAR(20) NOT NULL,
            {tableContent[4]} VARCHAR(20) NOT NULL,
            {tableContent[5]} VARCHAR(50) NOT NULL
        )
        """

        # Creating the DB
        database = sqlite3.connect(database)
        db = database.cursor()
        db.execute(newTable)

        time.sleep(2)

        database = "Database/Authentication.db"

        if os.path.isfile(database):
            print("")
            print("* Database Created")
            dbERR.destroy()
            mainFUN()
        else:
            print("")
        


    def cancel():
        dbERR.destroy()
        
    global dbERR

    dbERR = tk.Tk(className=" Error - Database Missing")

    dbERRLBL = tk.Label(dbERR,text="Database Missing - Would you like to create a new one?")
    yesBTN = tk.Button(dbERR, text="Yes",command=createDB)
    noBTN = tk.Button(dbERR, text="No",command=cancel)

    dbERRLBL.grid(row="0",column="0")
    yesBTN.grid(row="2",column="1")
    noBTN.grid(row="2",column="2")

    dbERR.mainloop()

if os.path.isfile(database):
    mainFUN()
else:
    db_notfound()