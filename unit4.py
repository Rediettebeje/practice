# two pointer technique
# a function that takes two sorted lists and returns a single sorted 
# list with all the elements from the input lists

# plan
# create a function that takes two lists as input
# create two pointers, one for each list
# create an empty list to store the sorted elements
# iterate over the two lists
# compare the elements at the two pointers
# append the smaller element to the sorted list
# increment the pointer of the list from which the element was taken
# repeat the process until both lists are exhausted
# return the sorted list

# implement

def sortedList(num1,num2):
    pointer_num1 = 0
    pointer_num2 = 0

    sorted = []

    while pointer_num1 < len(num1) and pointer_num2 < len(num2):
        if num1[pointer_num1] < num2[pointer_num2]:
            sorted.append(num1[pointer_num1])
            pointer_num1 += 1
        else:
            sorted.append(num2[pointer_num2])
            pointer_num2 += 1
    return sorted

print(sortedList([1,4,6],[2,3,6]))



