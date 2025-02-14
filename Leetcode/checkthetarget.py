
# since the array is sorted , we can use two pointers,
# we start with the first and last number 1 + 15 = 16 > 13
# since sum is > target we move the right pointer 1 + 14 = 15 > 13
# 1+ 9 = 10 < 13 so now we have to move the left pointer to increase the sum
# 2 + 9 = 11 < 13, 4 + 9 = 13 = 13 so the numbers are 4 and 9 we know that since the array is sorted
# there are not other numbers in the array that give us the sum because if we move forward our left pointer
# the sum will be greater than the target the same with the right pointer since its decrease the sum



def check_for_target(nums,target):
    left = nums[0]
    right = len(nums)-1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            print(nums[left],nums[right])
            return True

        elif current > target:
            right -= 1
        else:
            left += 1

    return False



nu = [1, 2, 4, 6, 8, 9, 14, 15]
targ = 13

check = check_for_target(nu,targ)
print(check)

