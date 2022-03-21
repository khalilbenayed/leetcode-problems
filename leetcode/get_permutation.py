"""
https://leetcode.com/problems/permutation-sequence/

Max duration per problem:
    6 sessions of 25 minutes
    3 consecutive days
How to Find a good solution
    Understand the problem and build and intuition about it (1 session)
    Build a brute (1 sessions)
    Build an optimized solution (1-2 sessions)
    Read solutions (1 session)
    Implement 1 of the solutions on my own (1 session)

0 - Question:
Write the question here
1- listen carefully and think about all case (including edge cases)
2- draw example:
3- Brainstorm
    Data Structure:
        * Tree - yes/no
        * List - yes/no
        * Map - yes/no
    Algorithm:
        * Recursion - yes/no
        * Dynamic Programming: yes/no
        * Sorting: yes/no
    Simplify the problem:
    Breakdown the problem into subproblem.
4- Brute force
5- Optimize:
    Space complexity
       * try to operate on the actual string.
    Time complexity
        * try to minimize iterations
6: Possible solution - (Pseudo code)
    Solution 1:
    ...

    Solution 2:
    ...
"""

from math import factorial
from test_runner import TestRunner


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(n, k):
        nums = [i for i in range(1, n+1)]
        result = []
        k -= 1

        idx = k // factorial(len(nums)-1)

        while idx < len(nums):
            result.append(nums.pop(idx))
            if len(nums) == 0:
                return ''.join(list(map(lambda x: str(x), result)))
            k -= idx * factorial(len(nums))
            idx = k // factorial(len(nums) - 1)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[3, 3], [4, 9]]
solutions = [Solution1.run]
TestRunner.run(solutions, test_data)

"""
1234
1243
1324
1342
1423
1432
2134
2143
2314
2341
2413
2431
"""
