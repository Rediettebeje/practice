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



