class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0  # To store the maximum number of consecutive 1s
        current_count = 0  # To track the current streak of 1s

        for num in nums:
            if num == 1:
                current_count += 1  # Increment the streak
                max_count = max(max_count, current_count)  # Update max_count if needed
            else:
                current_count = 0  # Reset streak when a 0 is encountered

        return max_count

# Create an instance of the Solution class
solution = Solution()

# Test the function with a sample binary array
nums = [1, 1, 0, 1, 1, 1, 0, 1]
print("Maximum number of consecutive 1s:", solution.findMaxConsecutiveOnes(nums))
