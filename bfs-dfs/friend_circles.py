"""
https://leetcode.com/problems/friend-circles/

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
    def run(isConnected):
        # just find the total number of connected components
        n = len(isConnected)
        seen = [False] * n
        num_components = 0
        for i in range(n):
            if seen[i]:
                continue

            stack = [i]
            num_components += 1
            while len(stack) != 0:
                curr = stack.pop()
                seen[curr] = True
                for j in range(n):
                    if isConnected[curr][j] and not seen[j]:
                        stack.append(j)
        return num_components


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[[[1,1,0],[1,1,0],[0,0,1]]], [[[1,1,0],[1,1,1],[0,1,1]]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
