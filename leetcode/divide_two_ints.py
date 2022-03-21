"""
https://leetcode.com/problems/divide-two-integers/

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

MAX_INT = 2**31-1

class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(dividend, divisor):
        neg = 1
        if dividend * divisor < 0:
            neg = -1
        dividend, divisor = abs(dividend), abs(divisor)

        count, curr_sum = 0, 0
        while curr_sum < dividend:
            sub_count, sub_curr_sum = 1, divisor

            while True:
                if curr_sum + sub_curr_sum + sub_curr_sum < dividend:
                    sub_curr_sum += sub_curr_sum
                    sub_count += sub_count
                else:
                    break
            count += sub_count
            curr_sum += sub_curr_sum

        if curr_sum != dividend:
            count -= 1
        return min(neg * count, MAX_INT)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[10, 3], [-7, 3], [20, 3], [2147483648, 1]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
