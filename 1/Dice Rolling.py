import time,sys,random

yes = ['y','Y','Yes','yes','yea','yeah','Yea','Yeah','Hell Yes!']
no = ['n','N','No','no','nah','na','Nah','Na']

while True:
    try:
        print("")
        userInput = input("Would you like to roll the dice? (Y/N)\n-> ")
        if userInput==yes[-1]:
            print("")
            print("--> Cheater Mode <--")
            print("")
            print("The Dice is rolling")
            num1 = random.randint(1,100)
            num2 = random.randint(1,100)
            total = num1 + num2
            time.sleep(2)
            print(f"You have rolled a {num1} and a {num2}")
            print(f"Total - {total}")
        elif userInput in yes or userInput in no:
            if userInput in yes:
                print("")
                print('The Dice is rolling')
                num1 = random.randint(1,6)
                num2 = random.randint(1,6)
                total = num1 + num2
                time.sleep(2)
                print(f"You have rolled a {num1} and a {num2}")
                print(f"Total - {total}")
            elif userInput in no:
                print("")
                print("[X] Game has been stopped")
                sys.exit()
        else:
            print("")
            print("[X] Invalid Argument - Please Try Again")
    except KeyboardInterrupt:
        print("")
        print("[X] Game has been stopped")
        sys.exit()
