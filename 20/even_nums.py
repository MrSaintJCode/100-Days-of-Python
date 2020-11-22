# https://www.udemy.com/course/100-days-of-code/
# Day - 5 | 21/11/2020
# By - Justin St-Laurent 

# Adding Even Numbers
def add_evens():
    total = 0
    for num in range(0, 101, 2):
        total += num
    return total
W
if __name__ == '__main__':
    print(add_evens())