"""
Task 1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


class Solution:
    def running_sum(self, nums: list[int]) -> list[int]:
        new_nums = []
        for i in range(0, len(nums)):
            new_nums.append(sum(nums[0:i + 1]))
        return new_nums

# Example:
# Input:
# my_array = [1, 2, 3, 4]
# solution = Solution()
# print(solution.running_sum(my_array))
# Output: [1,3,6,10]
