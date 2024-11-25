class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared_num = []
        
        # Square each number
        for num in nums:
            squared_num.append(num ** 2)
        
        # Sort the squared numbers
        sorted_num = sorted(squared_num)
        
        # Return the sorted list
        return sorted_num

# Example usage:
solution = Solution()  # Create an instance of the Solution class
nums = [-4, -1, 0, 3, 10]
# Call the method using the instance
output = solution.sortedSquares(nums)
print(output)  # Output: [0, 1, 9, 16, 100]
