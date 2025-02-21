# creating a function
def hello_world():
    print("helloworld!")

hello_world() # calling


def todays_mood():
    mood = "😆"
    print("Today's mood: " + mood)

todays_mood()

# problem3
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu("🍕")

# problem 4
def sum(a, b):
    return a + b

sumof = sum(13,27)
print(sumof * 2)

# problem5
def product(a,b):
    return a * b

print(product(22,7))

# function classify_age() that takes an integer age as a parameter and returns "child" if the age is less
#  than 18, and returns "adult"
def classify_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"

print(classify_age(17))
print(classify_age(19))

# Write a function named what_time_is_it() that takes 
# an integer hour as a parameter

def what_time_is_it(hour):
    if hour == 2:
        return "taco time"
    elif hour == 12:
        return "peanut butter jelly time"
    else:
        return "nap time"

print(what_time_is_it(2))
print(what_time_is_it(7))
print(what_time_is_it(12))

# a function called blackjack() that takes an integer score as a parameter.
# If score equals 21, print "Blackjack!".
# If score is greater than 21, print "Bust!".
# If score is greater than or equal to 17 and less than 21, print "Nice hand!".
# If score is less than 17, print "Hit me!"

def blackjack(score):
    if score == 21:
        print( "Blackjack")
    elif score > 21:
        print("Bust")
    elif score >= 17 and score < 21:
        print("Nice hand")
    else:
        print("Hit me")

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)

# a function get_first() that takes in a list as a parameter and 
# returns the first item in the list. Return None if the list is empty.

def get_first(list):
    if len(list) == 0:
        return "None"
    return list[0]

print(get_first([1,2,3,4]))

# a function get_last() that takes in a list as a parameter and 
# returns the last item in the list. Return None if the list is empty.

def get_last(list):
    if len(list) == 0:
        return "None"
    return list[len(list) - 1]

print(get_last([1,2,3,4]))

# a function counter() that uses the range function to print numbers between 1 and
# a given stop value (inclusive).

def counter(stop):
    for num in range(1,stop + 1):
        print(num)

counter(7)

# a function sum_ten() that returns the sum of numbers from 1 to 10.
def sum_ten():
    summ = 0
    for num in range(1,11):
        summ += num
        print(summ)

sum_ten()

# a function sum_positive_range() that returns the sum of numbers from 1
# to a given stop value (inclusive).

def sum_positive_range(stop):
    summ = 0
    for num in range(1,stop + 1):
        summ += num
        print(summ)


sum_positive_range(6)

#a function sum_range() that returns the sum of numbers from a given start
# value to a given stop value (inclusive).
def sum_range(start,stop):
    summ = 0
    for num in range(start,stop + 1):
        summ += num
        print(summ)

sum_range(3,9)

# a function print_negatives() that takes a list of integers lst and
# prints all negative numbers in the list.
def print_negatives(lst):
    for num in lst:
        if num < 0:
            print(num)


print_negatives([3,-2,2,1,-5])


# function doubled() that returns a new list of the doubled numbers.
def doubled(lst):
    for num in lst:
        return (num * 2)     # this will only return the first number in the list
        # The return statement inside the for loop causes the function to exit after processing the first element

doubled([1,2,3,4])  # this will only return 2

def doubled(lst):
    return [item * 2 for item in lst]  #return a new list containing the doubled values

lst = [1, 2, 3]
new_lst = doubled(lst)
print(new_lst)

# understand 
# function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by

# plan
# iterate through the list
# return a new list with each number multiplied by -

# implement
def flip_sign(lst):
    return [  num * 1 for num in lst]

lstt = [1,-2,-3,4]
flipped_lst = flip_sign(lstt)
print(flipped_lst)

# understand
# a function max_difference() that takes in a list of integers lst and returns
#  the difference between the smallest and largest value in the list.

# plan
# intialize two variables to store the smallest and largest value to zero
# iterate through the list
# compare the current value with the largest value
# if the current value is greater, update the largest value
# compare the current value with the largest value
# if the current value is smaller, update the smallest value
# return the difference between the largest and smallest value

# implement
def max_difference(lst):
    largest = 0
    smallest = 0

    for num in lst:
        if num > largest:
            largest = num
        if num < largest:
            smallest = num
    result = largest - smallest
    return result

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

