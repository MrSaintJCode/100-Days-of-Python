import tkinter as tk
import time,sys,datetime
import sqlite3
import os.path
import random
import smtplib as mail

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
    forgotpassBTN = tk.Button(loginPAN,text="Forgot Password",command=forgotpass,fg="Blue",highlightthickness = 0, bd = 0)
    nothing1 = tk.Label(loginPAN,text=" ")

    # Grid
    loginUsernameLBL.grid(row="1",column="1")
    loginUsernameEntry.grid(row="1",column="2")
    
    loginPasswordLBL.grid(row="3",column="1")
    loginPasswordEntry.grid(row="3",column="2")

    nothing1.grid(row="2",column="1")
    backBTN.grid(row="5",column="1")
    loginBTN.grid(row="5",column="2")
    forgotpassBTN.grid(row="4",column="2")

    loginPAN.mainloop()




global forgotpass

def forgotpass():
    try:
        server = mail.SMTP('smtp.gmail.com', 587)
        print("")
        print(f"* {server.ehlo()}")
        print("")
        print(f"* {server.starttls()}")
    except:
        print("")
        print("* Cannot establish connection to the SMTP server")
        sys.exit()


    def newPass():
        forgotpassPAN.destroy()

        # Update table with that user password
        pinInfo = pinEntry.get()

        if randomPIN == pinInfo:
            pinPAN.destroy()
            def changepassSQL():
                password = changepassEntry1.get()
                confirmpassword = changepassEntry2.get()
                

                if password == confirmpassword:
                    print("")
                    print("* Password Match")
                    with sqlite3.connect(database) as db:
                        cursor = db.cursor()
                    cursor.execute('''UPDATE Users SET Password = ? WHERE Email = ?''', (password, User_Email))
                    db.commit()
                    time.sleep(2)
                    print("")
                    print("* Password has been changed")

                    def clean():
                        passPAN.destroy()
                        changepassPAN.destroy()

                    passPAN = tk.Tk(className=" Password Changed")
                    passLBL = tk.Label(passPAN, text="Password has been changed")
                    passBTN =  tk.Button(passPAN,text="Ok",command=clean)

                    passLBL.pack()
                    passBTN.pack()
                    passPAN.mainloop()
                else:
                    print("")
                    print("* Password Doesn't Match")


            print("")
            print(f"* {randomPIN} Accepted")
            changepassPAN = tk.Tk(className=" Change Password")
            #changepassLBL = tk.Label(changepassPAN,text="Change your password")
            changepassBTN = tk.Button(changepassPAN,text="Apply", command=changepassSQL)

            changepassLBL1 = tk.Label(changepassPAN, text="Password")
            changepassLBL2 = tk.Label(changepassPAN, text="Confirm Password")

            changepassEntry1 = tk.Entry(changepassPAN, show="*")
            changepassEntry2 = tk.Entry(changepassPAN, show="*")

            changepassLBL1.grid(row="1", column="1")
            changepassEntry1.grid(row="1",column="2")

            changepassLBL2.grid(row="2",column="1")
            changepassEntry2.grid(row="2",column="2")

            changepassBTN.grid(row="3",column="2")

            changepassPAN.mainloop()

        else:
            print("")
            print(f"* {pinInfo} Incorrect Pin")
            errPAN = tk.Tk(className=" Error")
            errLBL = tk.Label(errPAN, text="Incorrect Pin")
            errBTN = tk.Button(errPAN,text="Ok",command=errPAN.destroy)
            
            errLBL.pack()
            errBTN.pack()
            errPAN.mainloop()
    

    def sendEmail():
        # Check if email is connected with a account that exist
        # Then create a random digit to send to that email 


        with sqlite3.connect(database) as db:
            cursor = db.cursor()

        global User_Email
        User_Email = forgotpassEntry.get()
        find_email = ("SELECT * FROM Users WHERE Email = ?")
        cursor.execute(find_email,[(User_Email)])
        results = cursor.fetchall()

        if results:
            gmail_user = "#"
            gmail_password = "#"
            try:
                global randomPIN
                randomPIN = f"{random.randint(100,999)} {random.randint(100,999)}"
                sent_from = "#"
                to = User_Email
                subject = "Password Reset"
                body = f"Please use the following code to verify: {randomPIN}"

                email_text = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sent_from, ", ".join(to), subject, body)
                

                server = mail.SMTP_SSL('smtp.gmail.com', 465)
                print("")
                print(f"* {server.ehlo()}")
                print("")
                print(f"* {server.login(gmail_user,gmail_password)}")
                server.sendmail(sent_from, to, email_text)
                print("")
                print(f"* Email sent to {User_Email}")

                # Pin Entry
                global pinPAN
                global pinEntry
                pinPAN = tk.Tk(className=" Email Pin")
                pinLBL = tk.Label(pinPAN,text="Enter Pin from Email")
                pinEntry = tk.Entry(pinPAN)
                pinBTN = tk.Button(pinPAN, text="Reset",command=newPass)

                pinLBL.pack()
                pinEntry.pack()
                pinBTN.pack()
                pinPAN.mainloop()

            except:
                print("")
                print("* An Error Occured")
        else:
            errPAN = tk.Tk(className=" Error")
            errLBL = tk.Label(errPAN, text="Email Doesn't Exist")
            errBTN = tk.Button(errPAN,text="Ok", command=errPAN.destroy)
            errLBL.pack()
            errBTN.pack()
            errPAN.mainloop()

        



    
    forgotpassPAN = tk.Tk(className=" Forgot Password")
    forgotpassLBL = tk.Label(forgotpassPAN,text=" Email")
    forgotpassEntry = tk.Entry(forgotpassPAN)
    forgotpassBTN = tk.Button(forgotpassPAN,text="Submit",command=sendEmail)

    forgotpassLBL.grid(row="1",column="1")
    forgotpassEntry.grid(row="1",column="2")
    forgotpassBTN.grid(row="2",column="2")



    forgotpassPAN.mainloop()


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