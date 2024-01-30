"""
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.

"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        my_array = ["1"] * n
        for i in range(0, n):
            my_array[i] = str(i + 1)
            if (i + 1) % 3 == 0:
                my_array[i] = "Fizz"
            if (i + 1) % 5 == 0:
                my_array[i] = "Buzz"
            if (i + 1) % 5 == 0 and (i + 1) % 3 == 0:
                my_array[i] = "FizzBuzz"
        return my_array

# n = 15
# solution = Solution()
# print(solution.fizzBuzz(n))
