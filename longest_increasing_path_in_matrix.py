"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

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
        dp[i][j] = longest increasing path, longest decreasing path
    """
    @staticmethod
    def run(matrix):
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])

        dp = [[None] * n for _ in range(m)]

        def dfs(matrix, row, col, memo):
            if not memo[row][col]:
                memo[row][col] = 1 + max(
                    dfs(matrix, row-1, col, memo) if row and matrix[row][col] > matrix[row-1][col] else 0,
                    dfs(matrix, row, col-1, memo) if col and matrix[row][col] > matrix[row][col-1] else 0,
                    dfs(matrix, row+1, col, memo) if row < m-1 and matrix[row][col] > matrix[row+1][col] else 0,
                    dfs(matrix, row, col+1, memo) if col < n-1 and matrix[row][col] > matrix[row][col+1] else 0)
            return memo[row][col]
        return max(
            [dfs(matrix, r, c, dp) for r in range(m) for c in range(n)])


directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    DFS with dp
    dp[i][j]: longest increasing sequence from (i, j)
    """
    @staticmethod
    def run(matrix):
        pass


test_data = [[[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]], [[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]], [[[7,8,9],
      [9,7,6],
      [7,2,3]]], [[[1,2]]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
