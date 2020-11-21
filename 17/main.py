# https://www.udemy.com/course/100-days-of-code/
# Day - 2 | 21/11/2020
# By - Justin St-Laurent 

# Tip Calculator
def divide(total, num_guests):
    split_value = total / num_guests
    return split_value

def tip(split_value, tip_input):
    percentage = tip_input / 100
    tip_total  = split_value * percentage
    total      = split_value + tip_total
    return total

if __name__ == '__main__':
    total       = float(input("Bill Total:"))
    num_guests  = float(input("Number of Guests:"))
    split_value = divide(total, num_guests)
    tip_input   = float(input(f"Your Total is {split_value}, what would you like to tip:"))
    total       = tip(split_value, tip_input)
    print(f"Your Total is: {total:.2f}")
