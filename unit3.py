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
        
     





