# Call the function so that it prints out the following to the 
# console (without calling the function more than once):

def count_mississippi(limit):
    for num in range(1, limit):
	    print( f"{num} mississippi")

count_mississippi(6)

# Write a function swap_ends() that accepts a string my_str as a parameter and returns
#  a new string where the first and last characters from my_str are swapped.

def swap_ends(my_str):
    # my_str[1:-1] is the string without the first and last characters
    # my_str[-1] is the last character
    # my_str[0] is the first charactergit
    return my_str[-1] + my_str[1:-1] + my_str[0]

print(swap_ends("hello"))

# Write a function is_pangram() that takes in a string my_str as a parameter 
# and returns True if the string is a pangram and False if not. 
# A pangram is a sentence containing every letter in the English alphabet.

def is_pangram(my_str):
     # set() returns a set of unique characters in the string
     result = set()
     for char in my_str:
          # isalpha() checks if the character is an alphabet
          if char.isalpha():
               result.add(char.lower())
          if len(result) == 26:
            return True
     return False

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

# Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    # [::-1] reverses the string
    return my_str[::-1]

my_str = "live your life"
print(reverse_string(my_str))


#Takes in a string 
# we need to reverse the letter of the strings 
# We must target the characters; maybe split by "-"
# we would reverse the string
#2 point method, only move pointer when at a letter 
def reverse_only_letters(s):
    point1=0
    point2=len(s)-1
    newS=list(s)
    while point1<point2:
        if (newS[point1].isalpha()) and newS[point2].isalpha():
            temp=newS[point1]
            newS[point1]=newS[point2]
            newS[point2]=temp
            point1+=1
            point2-=1
        if(newS[point1].isalpha()) and not newS[point2].isalpha():
            point2-=1
        if(newS[point2].isalpha()) and not newS[point1].isalpha():
            point1+=1
    newVal="".join(newS)
    return newVal
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)


# we have change the strings to integers by looping through the list of nums 
# we also need a val that incruments as we go 
# return that val 
def sum_of_number_strings(nums):
    total=0
    for num in nums:
        total+=int(num)
    return total
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
#Problem 2
# Empty list 
# we iterate through the list to check if already in the new list 
def remove_duplicates(nums):
    no_dups=[]
    for num in nums:
        if num not in no_dups:
            no_dups.append(num)
    return no_dups
nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
# we have change the strings to integers by looping through the list of nums 
# we also need a val that incruments as we go 
# return that val 
def sum_of_number_strings(nums):
    total=0
    for num in nums:
        total+=int(num)
    return total
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

#Takes in a string 
# we need to reverse the letter of the strings 
# We must target the characters; maybe split by "-"
# we would reverse the string
#2 point method, only move pointer when at a letter 
def reverse_only_letters(s):
    point1=0
    point2=len(s)-1
    newS=list(s)
    while point1<point2:
        if (newS[point1].isalpha()) and newS[point2].isalpha():
            temp=newS[point1]
            newS[point1]=newS[point2]
            newS[point2]=temp
            point1+=1
            point2-=1
        if(newS[point1].isalpha()) and not newS[point2].isalpha():
            point2-=1
        if(newS[point2].isalpha()) and not newS[point1].isalpha():
            point1+=1
    newVal="".join(newS)
    return newVal
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)


# we have change the strings to integers by looping through the list of nums 
# we also need a val that incruments as we go 
# return that val 
def sum_of_number_strings(nums):
    total=0
    for num in nums:
        total+=int(num)
    return total
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
#Problem 2
# Empty list 
# we iterate through the list to check if already in the new list 
def remove_duplicates(nums):
    no_dups=[]
    for num in nums:
        if num not in no_dups:
            no_dups.append(num)
    return no_dups
nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
# we have change the strings to integers by looping through the list of nums 
# we also need a val that incruments as we go 
# return that val 
def sum_of_number_strings(nums):
    total=0
    for num in nums:
        total+=int(num)
    return total
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)


word = "encourage"

char_count = {}
for char in word:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

# invalid syntax, we cannot add a list to a string 
# char_count = ['e'] += 2
print(char_count)

# we cannot change the value of a string by indexing
# greeting[7] = 'w'
# print(greeting)


# ignore whitespace and write a func that take a string and returns a dict with the count of each letter
def count_letters(word):
    char_count = {}
    for char in word:
        if char != " ":
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count

word = "hello world"
print(count_letters(word))
