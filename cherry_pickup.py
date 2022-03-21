"""
https://leetcode.com/problems/cherry-pickup/

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

    DP:
    matrix[i][j]: max at cell (i, j)
    """
    @staticmethod
    def run(grid):
        if grid[0][0] == -1:
            return 0

        m, n = len(grid), len(grid[0])
        matrix = [[0] * n for _ in range(m)]
        matrix[0][0] = grid[0][0]

        def run_dp():
            # fill first row and column
            for j in range(1, n):
                if grid[0][j] != -1:
                    matrix[0][j] = grid[0][j] + matrix[0][j-1] if matrix[0][j-1] != -1 else -1
                else:
                    matrix[0][j] = -1
            for i in range(1, m):
                if grid[i][0] != -1:
                    matrix[i][0] = grid[i][0] + matrix[i-1][0] if matrix[i-1][0] != -1 else -1
                else:
                    matrix[i][0] = -1

            # fill rest of matrix
            for i in range(1, m):
                for j in range(1, n):
                    if grid[i][j] != -1:
                        if matrix[i-1][j] == matrix[i][j-1] == -1:
                            matrix[i][j] = -1
                        else:
                            matrix[i][j] = grid[i][j] + max(matrix[i-1][j], matrix[i][j-1])
                    else:
                        matrix[i][j] = -1
            return matrix[m-1][n-1] if matrix[m-1][n-1] != -1 else 0

        cherries = run_dp()
        if cherries == 0:
            return 0

        # remove cherries on path and clean matrix
        x, y = m-1, n-1
        while x >= 0 and y >= 0:
            grid[x][y] = 0
            if y == 0 or (x > 0 and matrix[x - 1][y] >= matrix[x][y - 1]):
                x -= 1
            else:
                y -= 1
        matrix = [[0] * n for _ in range(m)]
        print(grid)
        return cherries + run_dp()


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    DP:
    matrix[m][r1][r2]: max after m steps with incoming/outgoing paths ending at rows r1/r2
    m: 1 -> 2n-1
    """
    @staticmethod
    def run(grid):
        if grid[0][0] == -1:
            return 0

        n = len(grid)
        matrix = [[-1] * n for _ in range(n)]
        matrix[0][0] = grid[0][0]

        for m in range(1, 2*n-1):
            new_matrix = [[-1] * n for _ in range(n)]
            for r1 in range(1, n):
                for r2 in range(1, n):
                    c1, c2 = m - r1, m - r2
                    if 0 <= c1 < n and 0 <= c2 < n and grid[r1][c1] != -1 and grid[r2][c2] != -1:
                        new_matrix[r1][r2] = matrix[r1][r2]
                        if r1 > 0:
                            new_matrix[r1][r2] = max(new_matrix[r1][r2], matrix[r1-1][r2])
                        if r2 > 0:
                            new_matrix[r1][r2] = max(new_matrix[r1][r2], matrix[r1][r2-1])
                        if r1 > 0 and r2 > 0:
                            new_matrix[r1][r2] = max(new_matrix[r1][r2], matrix[r1-1][r2-1])
                        if new_matrix[r1][r2] == -1:
                            continue
                        new_matrix[r1][r2] += grid[r1][c1] + (grid[r1][c1] if r1 != r2 else 0)
            matrix = new_matrix
        return matrix[n-1][n-1] if matrix[n-1][n-1] != -1 else 0


test_data = [[
            [[0, 1, -1],
             [1, 0, -1],
             [1, 1,  1]]], [
            [[1, 1, -1],
             [1, -1, 1],
             [-1, 1, 1]]], [
            [[1, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1],
             [1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1]]]
]
solutions = [Solution2.run]
TestRunner.run(solutions, test_data)
