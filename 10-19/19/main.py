# https://www.udemy.com/course/100-days-of-code/
# Day - 4 | 21/11/2020
# By - Justin St-Laurent 

# Rock, Paper, Scissors Game
import random
def game(player_choice):
    # 1 - Rock
    # 2 - Paper
    # 3 - Scissors
    pc_choice = random.randint(1, 3)
    if pc_choice == 1:
        _rock = '''
            _______
        ---'   ____)
             (_____)
             (_____)
             (____)
        ---.__(___)
        '''
        print(_rock)
        print("PC has played: Rock")
        if player_choice.lower() == "paper":
            return "Player has won!"
        elif player_choice.lower() == "scissors":
            return "PC has won!"
        elif player_choice.lower() == "rock":
            return "It's a tie!"
    elif pc_choice == 2:
        _paper = '''
            _______
        ---'    ____)
                ______)
                _______)
                _______)
        ---.__________)
        '''
        print(_paper)
        print("PC has played: Paper")
        if player_choice.lower() == "paper":
            return "It's a tie!"
        elif player_choice.lower() == "scissors":
            return "Player has won!"
        elif player_choice.lower() == "rock":
            return "PC has won!"
    elif pc_choice == 3:
        _scissors = '''
            _______
        ---'   ____)____
                  ______)
               __________)
                (____)
        ---.__(___)
                '''
        print(_scissors)
        print("PC has played: Scissors")
        if player_choice.lower() == "paper":
            return "PC has won!"
        elif player_choice.lower() == "scissors":
            return "It's a tie!"
        elif player_choice.lower() == "rock":
            return "Player has won!"
    return "Not a valid option"

if __name__ == '__main__':
    print("Welcome to the Rock, Paper, Scissors Game")
    player_choice = input("Player Choice [Rock, Paper, Scissors]:")
    print(game(player_choice))
