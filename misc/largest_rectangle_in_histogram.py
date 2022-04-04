"""
j
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

    Brute force: O(n^2)
    """
    @staticmethod
    def run(heights):
        n = len(heights)
        max_area = 0
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(heights):
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            j, area = i, 0
            while len(stack) != 0 and height < stack[-1][1]:
                j, h = stack.pop()
                area = max(area, (i-j) * h)
            max_area = max(max_area, area)
            stack.append((j, height))

        area = 0
        while len(stack) != 0:
            j, h = stack.pop()
            area = max(area, h * (len(heights) - j))

        return max(max_area, area)


test_data = [[[2, 1, 5, 6, 2, 3]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
