"""
https://leetcode.com/problems/coloring-a-border/

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


directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(grid, r0, c0, color):
        m, n = len(grid), len(grid[0])
        component_color = grid[r0][c0]

        def is_in_border(r, c):
            if r == 0 or r == m-1 or c == 0 or c == n-1:
                return True
            for i, j in directions:
                if grid[r+i][c+j] != component_color:
                    return True
            return False

        # first find the border of the component
        border, seen = set(), set()
        stack = [(r0, c0)]
        while len(stack) != 0:
            r, c = stack.pop()
            if is_in_border(r, c):
                border.add((r, c))
            for i, j in directions:
                nr, nc = r+i, c+j
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == component_color and (nr, nc) not in seen:
                    stack.append((nr, nc))
            seen.add((r, c))

        # now color the border
        for r, c in border:
            grid[r][c] = color

        return grid

class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[[[1, 1], [1, 2]], 0, 0, 3], [[[1, 2, 2], [2, 3, 2]], 0, 1, 3], [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
