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

# a function named mystery() that takes two lists of integers as parameters 
# and returns a new list that contains all the numbers from the first list followed
#  by all the numbers from the second list.

def mystery(lst1,lst2):
    for num in lst2:
        lst1.append(num)
    return lst1

output = mystery([1,2,3],[4,5,6])
print(output)

# a function named count_negatives() that takes a list of integers as 
# a parameter and returns the number of negative numbers in the list.

def count_negatives(lst):
    count = 0
    for num in lst:
        if num < 0:
            count += 1
    return count
# test the function
print(count_negatives([1,-2,3,-4,5]))


# a function named find_min() that takes a list of integers as a 
# parameter and returns the smallest number in the list.
def find_min(lst):
    min = lst[0]
    for num in lst:
        if num < min:
            min = num
    return min

print(find_min([3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]))

# understand
# a function that takes a list of integers numbers and an integer threshold as a parameter and 
# returns the number of items in  numbers that are less than threshold.

# plan
# 1. initialize a counter variable to 0
# 2. iterate through the list
# 3. for each number in the list, check if it is less than the threshold
# 4. if it is, increment the counter by 1
# 5. return the counter

# implement
def count_below_threshold(numbers, threshold):
    counter = 0
    for num in numbers:
        if num < threshold:
            counter += 1
    return counter

# if we want to return the numbers
# plan
# 1. initialize an empty list to store the numbers that are less than the threshold
# 2. iterate through the list
# 3. for each number in the list, check if it is less than the threshold
# 4. if it is, add it to the list
# 5. return the list

# implement
def count_less_than(numbers, threshold):
    less_threshold = []

    for num in numbers:
        if num < threshold:
            less_threshold.append(num)
    return less_threshold


numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)
    

# understand

# a function that takes a list of integers and returns a list of even numbers
# plan
# 1. initialize an empty list to store the even numbers
# 2. iterate through the list
# 3. for each number in the list, check if it is even
# 4. if it is, add it to the list
# 5. return the list

# implement
def get_evens(lst):
    even_no = []
    for num in lst:
        if num % 2 == 0:
            even_no.append(num)
    return even_no


lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)



# understand
# a fun that prints out multiplies of 5 b/n 1 and 100

# plan
# iterate through the range of numbers from 1 to 100
# check if the numbers is a multiplies of 5
# if it is, print the number

# implement
def multiples_of_five():
    for number in range(1,101):
        if number % 5 == 0:
            print(number)

# multiples_of_five()

# understand
# a function that takes a number as a parameter and returns a list of all divisors of the number

# plan
# 1. initialize an empty list to store the divisors
# 2. iterate through the range of numbers from 1 to the input number
# 3. for each number in the range, check if it is a divisor of the input number
# 4. if it is, add it to the list
# 5. return the list

# implement
def find_divisors(n):
    divisors = []
    for num in range(1,n + 1):
        if n % num == 0:
            divisors.append(num)
    return divisors


lst = find_divisors(6)
print(lst)
