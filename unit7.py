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


# print(factorial(5))
#
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))

