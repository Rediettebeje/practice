# // operator or floor division, x // y
# returns the result of x divided by y rounded
# down to the nearest integer

# print(5//2) # prints 2
# print(10//2) # prints 5

# recursion, is the process of a function calling itself
        # it's a way to repeatedly execute a chunk of code

def count_recursive(num):

    if num == 1:
        return # base case, end condition
    else:
        count_recursive(num-1)
    print(f"count{num}")

# count_recursive(5)


def is_odd(n):
   # multiple base cases
    if n == 0:
        return False
    if n == 1:
        return True

    else:
        return is_odd(n - 2)

test = is_odd(5)
# is_odd(5) → is_odd(3)
# is_odd(3) → is_odd(1)
# is_odd(1) → returns True
# print(test)
teste = is_odd(6)
# is_odd(6) → is_odd(5)
# is_odd(5) → is_odd(3)
# is_odd(3) → is_odd(1)
# is_odd(1) → returns True
# print(teste)

def count_evens(lst):

    if not lst:
        return 0
    if lst[0] % 2 == 0:
        return 1 + count_evens(lst[1:]) # lst[1:] means: Give me a new list that starts from index 1 to the end.
    else:
        return count_evens(lst[1:])

# output = count_evens([1,2,3,4])
# print(output)

def partition_even_odd(lst):
    return recursive_partition(lst,[],[])
def recursive_partition(lst,evens,odds):
    if not lst:
        return evens,odds
    if lst[0] % 2 == 0:
        evens.append(lst[0])
    else:
        odds.append(lst[0])
    return recursive_partition(lst[1:],evens,odds)

# print(partition_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n - 1)


# repeat_hello(5)

# def repeat_hello(n):
#     for num in range(n):
#         print("HELLO")

# repeat_hello(5)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(4))
#
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

# print(sum_list([1, 2, 3, 4, 5]))

#understanding:
# a fun that takes a list of number and returns their sum
# what if the list is empty, we return 0

# Planning:
# 1. Check if the list is empty
# 2. If it is, return 0
# 3. If not, add the first number [0]
# 4. Call the recursive function with the rest of the list [1:]

# note lst[1:] — slicing from index 1 onward,
# lst[:1] would give only the first element

def sum_list(lst):
    if len(lst) == 0:
        return 0
    
    return lst[0] + sum_list(lst[1:])

lst = [1,2,3,4,5] 
print(sum_list(lst))
	

def is_power_of_two(n):
    if n == 1:
            return True
    if n < 1 or n %2 != 0:    
            return False
    return is_power_of_two(n // 2)

print(is_power_of_two(8)) # True
print(is_power_of_two(6)) # False


def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst) - 1
	# While left pointer is less than right pointer:
    while left <= right:
		# Find the middle index of the array
        middle = (left + right) // 2
		
		# If the value at the middle index is the target value:
        if lst[middle] == target:
			# Return the middle 
            return middle
		# Else if the value at the middle index is less than our target value:
        elif lst[middle] < target:
			# Update pointer(s) to only search right half of the list in next loop iteration
            left = middle + 1
		# Else
        else:
			# Update pointer(s) to only search left half of the list in next loop iteration
            right = middle - 1
	
	# If we search whole list and haven't found target value, return -1
    return -1
# Test cases     
print(binary_search([1, 2, 3, 4, 5], 3)) # Output: 2
print(binary_search([1, 2, 3, 4, 5], 6)) # Output: -1


def find_last(lst, target):
	# Initialize a left pointer to the 0th index in the list
    left = 0
	# Initialize a right pointer to the last index in the list
    right = len(lst) - 1
	# While left pointer is less than right pointer:

    # create a variable to store the last occurrence of the target value
    last_occur = -1


    while left <= right:
		# Find the middle index of the array
        middle = (left + right) // 2
		
		# If the value at the middle index is the target value:
        if lst[middle] == target:
            # Store the middle index in last_occur variable
            last_occur = middle
			# Update pointer(s) to only search right half of the list in next loop iteration
            left = middle + 1
		# Else if the value at the middle index is less than our target value:
        elif lst[middle] < target:
			# Update pointer(s) to only search right half of the list in next loop iteration
            left = middle + 1
		# Else
        else:
			# Update pointer(s) to only search left half of the list in next loop iteration
            right = middle - 1
	
	# return the last occurrence of the target value
    return last_occur

# Test cases     
print(find_last([1, 3, 5, 7, 9, 11, 11, 13, 15], target = 11)) # Output: 6
print(find_last([1, 3, 5, 7, 9, 11, 11, 13, 15], target = 6)) # Output: -1

    
