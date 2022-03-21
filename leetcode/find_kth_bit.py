"""
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

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

from test_runner import TestRunner


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(n, k):
        def fn(n, k):
            print(n, k)
            if n == 1:
                return '0'

            # first find length of binary string
            length = 2 ** n - 1
            mid = length // 2
            if k < mid:
                return fn(n-1, k)
            elif k == mid:
                return '1'
            else:
                return '0' if fn(n-1, length - k - 1) == '1' else '1'

        return fn(n, k-1)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[3, 1], [4, 11], [1, 1], [2, 3]]
solutions = [Solution1.run]
TestRunner.run(solutions, test_data)
