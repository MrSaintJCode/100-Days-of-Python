# https://www.udemy.com/course/100-days-of-code/
# Day - 7 | 23/11/2020
# By - Justin St-Laurent 

# Hangman
import random
from ascii_hangman import HANGMANPICS

_header = '''
                     +---+
    Hangman          |   |   
        Game         O   |
                    /|\  |
                    / \  |
                         |
                     =========
'''

def generate_word():
    word_list = ["baboon"]
    return random.choice(word_list)
    
def start_game(word):
    # Creating _ _ _ _ _ and words into an arr
    words  = list(word)
    blanks = []
    for blank in words:
        blanks.append(" _ ")

    # There are 7 types of hangman status - ascii_hangman.py
    hangman_status = 0
 
    while True:
        print(chr(27) + "[2J")
        blanks_display = ''.join(blanks)
        _output = f"""
               {HANGMANPICS[hangman_status]}

        {blanks_display}
        """
        print(_output)
        
        if hangman_status == 7:
            print("Oh dear! You have lost the game")
            print(f"Word - {word}")
            break

        if blanks_display == word:
            print("You have won!")
            break

        guess = input("Guess a letter:").lower()
        if guess in words:
            # Guess is in the words list
            for index, char in enumerate(words):
                if char == guess:
                    blanks[index] = guess
        else:
            # Word isn't in the word list
            hangman_status += 1

        
if __name__ == '__main__':
    print(_header)
    start = input("Would you like to start a new game? (Y/N)")
    if start.lower() == "y" or start.lower() == "yes":
        word = generate_word()
        start_game(word)


