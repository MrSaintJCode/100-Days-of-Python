# https://www.udemy.com/course/100-days-of-code/
# Day - 5 | 22/11/2020
# By - Justin St-Laurent 

# Password Generator
import random

# Easy Level
def generate_pass(nr_letters, nr_symbols, nr_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("[+] Generating Password...")
    password      = ""
    password_list = []
    
    # Random letters
    for char in range(1, nr_letters + 1):
        random_char = random.choice(letters)
        password += random_char
        password_list.append(random_char)

    # Random symbols
    for sym in range(1, nr_symbols + 1):
        random_sym = random.choice(symbols)
        password += random_sym
        password_list.append(random_sym)

    # Random numbers
    for num in range(1, nr_numbers + 1):
        random_num = random.choice(numbers)
        password += random_num
        password_list.append(random_num)

    easy_password = password
    print(f"[✓] Easy Password Generated - {easy_password}")

    print("[+] Shuffling Password...")
    random.shuffle(password_list)
    hard_password = ''.join(password_list)
    return f"[✓] Hard Password Generated - {hard_password}"


if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password = generate_pass(nr_letters, nr_symbols, nr_numbers)
    print(password)
