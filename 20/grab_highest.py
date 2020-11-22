# https://www.udemy.com/course/100-days-of-code/
# Day - 5 | 21/11/2020
# By - Justin St-Laurent 

# High Score
def grab_highest(arr):
    highest_number = 0
    for item in arr:
        if item > highest_number:
            highest_number = item
    return highest_number

if __name__ == '__main__':
    student_scores = [78, 65, 89, 86, 55, 81, 91, 105]
    highest_number = grab_highest(student_scores)
    print(highest_number)