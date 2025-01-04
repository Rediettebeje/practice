# practice
<!-- ******************************************* -->
 # * max(x, y):

The * * max() * * function in Python takes two values (x and y) and returns the larger one.
For example:
max(3, 5)  # Returns 5
max(7, 2)  # Returns 7 


<!-- ******************************************* -->
to to compute the number of digits of a number we can either
convert it to a string or use mathematical operations to count the number of digits.

  # * digit_count = len(str(num))
   # * or  num //= 10 

<!-- ******************************************* -->
The expression num ** 2 in Python means raising the number num to the power of 2, or simply squaring num.

The ** operator in Python is the exponentiation operator.
 # * num ** 2 is equivalent to num *num

the list.append() method modifies the list in place and returns None. This is an important design choice in Python for in-place modification methods like append, extend, sort, etc. They update the original object but do not return the modified object.

squared_num = [1, 4]
squared_num.append(9)  # Adds 9 to the list
print(squared_num)  # Output: [1, 4, 9]

squared_num = [1, 4]
result = squared_num.append(9)  # result will be None
print(result)  # Output: None

 # * For list modification methods like append(), extend(), sort(), and reverse(), do not assign their results to the variable. They modify the list directly and return None