# https://www.udemy.com/course/100-days-of-code/
# Day - 5 | 21/11/2020
# By - Justin St-Laurent 

# Average Height
def calculate_average(arr):
    #total              = sum(arr)
    total = 0
    for item in arr:
        total += item
    #print(total)
     
    #number_of_elements = len(arr)
    number_of_elements = 0
    for item in arr:
        number_of_elements += 1
    #print(number_of_elements)

    average = round(total / number_of_elements)
    return average

if __name__ == '__main__':
    student_heights = [180, 124, 165, 173, 189, 169, 146]
    average = calculate_average(student_heights)
    print(average)