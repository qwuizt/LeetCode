"""
1672.
You are given an m x n integer grid accounts
where accounts[i][j] is the amount of money the i customer has in the j bank.
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
"""

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        list_wealthy = [sum(i) for i in accounts]
        return max(list_wealthy)


# my_array = [[1, 2, 3], [3, 2, 1]]
# solution = Solution()
# print(solution.maximumWealth(my_array))
