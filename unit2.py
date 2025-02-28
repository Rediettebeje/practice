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