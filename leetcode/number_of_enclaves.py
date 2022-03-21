"""
https://leetcode.com/problems/number-of-enclaves/

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

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """

    @staticmethod
    def num_enclaves(grid):
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])

        island_cells = set()
        continent_cells = set()

        def explore_land(x, y):
            visited = {(x, y)}
            stack = [(x, y)]
            is_island = True
            while len(stack) != 0:
                curr_x, curr_y = stack.pop()
                visited.add((curr_x, curr_y))

                for a, b in directions:
                    if curr_x+a < 0 or curr_x+a >= m or curr_y+b < 0 or curr_y+b >= n:
                        is_island = False
                        continue

                    if grid[curr_x+a][curr_y+b] and (curr_x+a, curr_y+b) not in visited:
                        stack.append((curr_x+a, curr_y+b))
            return visited, is_island

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                if val == 1 and (i, j) not in island_cells | continent_cells:
                    explored_cells, is_island = explore_land(i, j)
                    if is_island:
                        island_cells |= explored_cells
                    else:
                        continent_cells |= explored_cells
        return len(island_cells)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def num_enclaves(grid):
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])

        def explore_land(x, y):
            if grid[x][y] == 0:
                return
            stack = [(x, y)]
            while len(stack) != 0:
                curr_x, curr_y = stack.pop()
                grid[curr_x][curr_y] = 0

                for a, b in directions:
                    if 0 <= curr_x+a < m and 0 <= curr_y+b < n and grid[curr_x+a][curr_y+b] == 1:
                        stack.append((curr_x+a, curr_y+b))

        for i in range(m):
            explore_land(i, 0)
            explore_land(i, n-1)
        for j in range(n):
            explore_land(0, j)
            explore_land(m-1, j)

        return sum(sum(row) for row in grid)


test_data = [
    [[
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]], [[
        [0, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]]]
solutions = [Solution1.num_enclaves, Solution2.num_enclaves]
TestRunner.run(solutions, test_data)
