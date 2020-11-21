# https://www.udemy.com/course/100-days-of-code/
# Day - 3 | 21/11/2020
# By - Justin St-Laurent 

# Control Flow and Logical Operators
if __name__ == '__main__':
    player  = input("Player:")
    _header = (f'''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/______/
    *******************************************************************************
                          Welcome {player} to Tresure Island.
    ''')


    print(_header)
    choice = input("You're at a cross road. Where do you want to go? [Left / Right]\n")
    if choice.lower() == 'left':
        choice = input("You arrive at a lake. There is an island in the middle of the lake. Wait for a boat or swim accross? [Wait / Swim]")
        if choice.lower() == "wait":
            choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door would you like to go in? [Red / Yellow / Blue]")
            if choice.lower() == 'red':
                print(f"Oh dear! {player} has been set on fire! Game over.")
            elif choice.lower() == 'yellow':
                print(f"{player} found the tresure! You've won!")
            elif choice.lower() == "blue":
                print(f"Oh dear! {player} has been eaten by a dragon! Game over.")
            else:
                print(f"Oh dear! {player} has decided to stay and look at the doors! Game over.")
        else:
            print(f"Oh dear! {player} has been attacked by trout! Game over.")
    else:
        print(f"Oh dear! {player} has fallen into hole! Game over.")