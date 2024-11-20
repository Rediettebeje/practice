class Solution:
    def countNumbersWithEvenDigits(self, nums: list[int]) -> int:
        even_digit_count = 0
        
        # Iterate through each number in the list
        for num in nums:
            digit_count = 0
            # While the number is greater than 0
            while num > 0:
                num //= 10  # Perform integer division by 10
                digit_count += 1  # Increment the digit count

            # If the number of digits is even, increment the count
            if digit_count % 2 == 0:
                even_digit_count += 1

        return even_digit_count

# Example usage:
solution = Solution()
nums = [12, 345, 2, 6, 7896]
print(solution.countNumbersWithEvenDigits(nums))  # Output: 2
