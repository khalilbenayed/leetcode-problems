"""
https://leetcode.com/problems/brick-wall/

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
    Too slow
    """
    @staticmethod
    def run(wall):

        def crosses(width):
            ans = 0
            for row in wall:
                s = 0
                for brick in row:
                    s += brick
                    if s == width:
                        break
                    elif s > width:
                        ans += 1
                        break
            return ans

        seen = {sum(wall[0])}
        least_bricks = len(wall)
        for row in wall:
            width = 0
            for brick in row:
                width += brick
                if width not in seen:
                    least_bricks = min(least_bricks, crosses(width))
                    seen.add(width)
        return least_bricks


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(wall):
        wall_height, wall_width = len(wall), sum(wall[0])
        matches = {}
        for row in wall:
            width = 0
            for brick in row:
                width += brick
                if width != wall_width:
                    if width in matches:
                        matches[width] += 1
                    else:
                        matches[width] = 1
        return wall_height - max(matches.values()) if len(matches) != 0 else wall_height


test_data = [
    [[[1,2,2,1],
      [3,1,2],
      [1,3,2],
      [2,4],
      [3,1,2],
      [1,3,1,1]]],
    [[[1],
      [1],
      [1]]]
]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
