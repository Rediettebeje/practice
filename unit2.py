# a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.

# understand
# we are given a dictinary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.

# Plan
# check if the candidate is in votes dictionary
# if it is, increment the value by 1
# if it is not, add the candidiate to the dict with a value of 1
# return the updated dictionary

# implement

def cast_vote(votes, candidate):

    if candidate in votes.keys():
        votes[candidate] += 1
    else:
        votes[candidate] = 1
  

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

my_list = ['a', 'b', 'c', 'd']
# slicing to extract a portion of the list
# my_list[1:3] means "get elements from index 1 up to (but not including) index 3
print(my_list[1:3])

my_dict = {'a':[1,2], 'b':[3,4], 'c':[5,6]}

output = []

# When we iterate over my_dict in a for loop, it iterates over the keys by default.
for item in my_dict:
    output.append(item)

print(output)

# output = ['a', 'b', 'c']

# If we want to iterate over the values, we can use the values() method.
output = []
for item in my_dict.values():
    output.append(item)
print(output)
# output = [[1, 2], [3, 4], [5, 6]]

# If we want to iterate over both the keys and values, we can use the items() method.
output = []
for item in my_dict.items():
    output.append(item)
print(output)

# output = [('a', [1, 2]), ('b', [3, 4]), ('c', [5, 6])]


def get_top_player(dictionary):
    high_score = 0
    top_player = ""
    for name,score in dictionary.items():
        if score > high_score:
            high_score = score
            top_player = name
    return top_player

scores = {"Alice": 50, "Bob": 40, "Charlie": 60}
print(get_top_player(scores))
# output: "Charlie"

# understand

# we are given a list of numbers
# we need to check how many times the value appears in the list
# if the value appears more than one time, we return true, if not we return false
  
# Plan
# create a dictionary to store the count of each number
# iterate over the list
# if the number is in the dictionary, increment the value by 1
# if the number is not in the dictionary, add it to the dictionary with a value of 1
# 
# iterate over the dictionary
# if the value is greater than 1, return true
# if the loop completes, return false
#  implement
def count_appearances(lst):
    counts = {}
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for count in counts.values():
        if count > 1:
            return True
    return False


def frequency_greater_than_n(nums, n):
    # Write your code here
    
    dictt = {}
    
    for num in nums:
        if num in dictt:
            dictt[num] += 1
        else:
            dictt[num] = 1
    
    result = {}
    for key, value in dictt.items():
        if value > n:
            result[key] = value
            
    return result
        




nums = [1, 2, 2, 3, 3, 3, 4]
n = 1
print(frequency_greater_than_n(nums, n))