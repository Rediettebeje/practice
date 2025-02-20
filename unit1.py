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
