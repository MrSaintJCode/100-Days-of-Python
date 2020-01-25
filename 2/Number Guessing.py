import random
import time
import sys

minNum = 1
maxNum = 20
lives = 10

print("""
              _,;;.,_
     ,-;;,_  ;,',,,'''@
  ,;;``  `'\ |//``-:;,.
@`         ;^^^;      `'@
           :@ @:
           \ u /
  ,=,------)^^^(------,=,
  '-'-----/=====\-----'-'  
          \_____/              
      '`\ /_____                    
      `\  \_____/_
        \//_____\/|
        |        ||
        |        |'
        :________:`

--->  Guess The Number  <---
""")

number = random.randint(minNum,maxNum)

while lives > 0:
    try:
        print("")
        print(f"Lives - {lives}")
        try:
            guess = int(input(f"I am thinking of a number between {minNum} and {maxNum}\nGuess: "))
            if guess < minNum or guess > maxNum:
                print("")
                print(f"[X] The number must be between {minNum} and {maxNum}")
            else:
                if guess == number:
                    print("")
                    print("--> Winner Winner Chicken Dinner <--")
                    print(f"The number was {number}")
                    sys.exit()
                elif guess > number:
                    print("")
                    print(f"The number is LOWER than {guess}")
                    lives = lives - 1
                elif guess < number:
                    print("")
                    print(f"The number is HIGHER than {guess}")
                    lives = lives - 1
                
        except ValueError:
            print("")
            print("[X] Please enter a number")
            
    
    except KeyboardInterrupt:
        print("")
        print("[X] Closing...")
        sys.exit()
    
if lives == 0:
    print("")
    print("[X] You have died!")
    sys.exit()