import tkinter as tk
import time,sys,datetime
import sqlite3
import os.path

database = "Authentication.db"

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
        cursor.execute(find_user,[(Username)])
        results = cursor.fetchall()
        if results:
            userexistPAN = tk.Tk(className="Error")

            userexistPAN.mainloop()
        else:
            # Create the user
            if Password == ConfirmPassword:
                print("Good")
            else:
                print("Password doesnt match")



        
    # Back to main
    def goBack():
        registerPAN.destroy()


    
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


# def forgotpas():

def main():
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
        print("")

    def cancel():
        print("")

    dbERR = tk.Tk(className=" Error - Database Missing")

    dbERRLBL = tk.Label(dbERR,text="Database Missing - Would you like to create a new one?")
    yesBTN = tk.Button(dbERR, text="Yes",command=createDB)
    noBTN = tk.Button(dbERR, text="No",command=cancel)

    dbERRLBL.grid(row="0",column="0")
    yesBTN.grid(row="2",column="1")
    noBTN.grid(row="2",column="2")

    dbERR.mainloop()

if os.path.isfile(f"Database/{database}"):
    main()
else:
    db_notfound()