import sys
import time

def addition():
    num1 = int(input("First Number - "))
    num2 = int(input("Second Number - "))
    total = num1 + num2
    return total

def subtracting():
    num1 = int(input("First Number - "))
    num2 = int(input("Second Number - "))
    total = num1 - num2
    return total

def multiplication():
    num1 = int(input("First Number - "))
    num2 = int(input("Second Number - "))
    total = num1 * num2
    return total   

def division():
    num1 = int(input("First Number - "))
    num2 = int(input("Second Number - "))
    try:
        total = num1 / num2
        return total   
    except ZeroDivisionError:
        print("")
        print("[X] Can't divide by 0")
        sys.exit()

while True:
    try:
        try:
            print("")
            options = int(input("-> Text Calculator <-\n1) Addition\n2) Subtracting\n3) Multiplication\n4) Division\nOption: "))

            if options == 1:
                total = addition()
                print("")
                print(f"The total is {total}")
                time.sleep(3)   
            elif options == 2:
                total = subtracting()
                print("")
                print(f"The total is {total}")
                time.sleep(3)  
            elif options == 3:
                total = multiplication()
                print("")
                print(f"The total is {total}")
                time.sleep(3)  
            elif options == 4:
                total = division()
                print("")
                print(f"The total is {total}")
                time.sleep(3)  
            else:
                print("")
                print("[X] Please enter a valid option")


        except ValueError:
            print("")
            print("[X] Please enter a valid option")
    except KeyboardInterrupt:
        print("")
        print("[X] Closing...")
        sys.exit()