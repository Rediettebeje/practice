# list is sorted list of integers. target is an integer, assume n is representing the length of the list.
# if we use two pointers what would be the time complexity of the algorithm?
# if we use binary search what would be the time complexity of the algorithm?
# implement
# TIME COMPLEXITY OF THE Below is 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def mystery_function(n):
    if n== 0:
        return 0
    if n % 2 == 0:
        return 2 + mystery_function(n -1)
    else:
        return 3 + mystery_function(n - 1)

OUTPUT = mystery_function(2)
print(OUTPUT) 

def recursive_function(a, b):
    if  b < 0:
        return -1 * recursive_function(a, -b)
    if b == 0:
        return 0
    
    return a + recursive_function(a, b - 1)

OUTPUT = recursive_function(2, 3)
print(OUTPUT)
    
 

 # given an alphabtically sorted list of strings and a string val, return the index of the first occurrence of val in O(logn) time.

 # if val is not a name in names, return -1.
 # you may use the built_in index() function

def find_val(names, val):
    left, right = 0, len(names) - 1
    while left <= right:
        mid = (left + right) // 2
        if names[mid] == val:
            return mid
        elif names[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# names = ["Amal", "Beric", "Florin", "Julie", "Qin"]
# val = "Julie"
# OUTPUT 3

# names = ["Amal", "Beric", "Florin", "Julie", "Qin"]
# val = "Tabrez"

# output =  -1

# power function
# given two integers, x and n where n >=0, write a function power() that recursively computes x^n.

def power (x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * power(x, n - 1)


# GIVEN A LIST OF INTEGERS NUMS SORTED IN NON _ DECREASING ORDER, FIND THE START AND END POSITION OF A GIVEN TARGET VALUE return the results as a list in the form [start, end].
# if target is not found in nums, return [-1, -1].
# you must write an algorithm with O(log n) runtime complexity.

def search(nums, target):
    def find_start(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find_end(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    start = find_start(nums, target)
    end = find_end(nums, target)

    if start <= end:
        return [start, end]
    else:
        return [-1, -1]
    

# section B 

def mystery_function(arr,left,right,key):
    if right >= left:
        mid = left + ((right - left)) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return mystery_function(arr, left, mid - 1, key)
        else:
            return mystery_function(arr, mid + 1, right, key)
       
    return -1

# Example array and key
arr = [1, 3, 5, 7, 9, 11]
key = 7

# Call the function
result = mystery_function([1,2,3,4,5], 0, 4, 20)

# Output the result
print(result) 

def is_perfect_square(num):
    if num < 0:
        return False
    left, right = 0, num
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Example usage
print(is_perfect_square(16))  # True
print(is_perfect_square(14))  # False