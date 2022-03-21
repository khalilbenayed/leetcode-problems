"""
https://leetcode.com/problems/regions-cut-by-slashes/

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

direct_directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
left_diagonal = ((1, 1), (-1, -1))
right_diagonal = ((1, -1), (-1, 1))


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(grid):
        n = len(grid)
        mat = [[' '] * (2*n) for _ in range(2*n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '\\':
                    mat[2*i][2*j] = mat[2*i + 1][2*j + 1] = '*'
                elif grid[i][j] == '/':
                    mat[2*i][2*j + 1] = mat[2*i + 1][2*j] = '*'

        num_regions = 0
        n = 2*n

        def dfs(x, y, region_number):
            stack = [(x, y)]
            while len(stack) != 0:
                a, b = stack.pop()
                mat[a][b] = str(region_number)
                if a % 2 == b % 2:
                    directions = direct_directions + right_diagonal
                else:
                    directions = direct_directions + left_diagonal
                for i, j in directions:
                    if 0 <= a+i < n and 0 <= b+j < n and mat[a+i][b+j] == ' ':
                        stack.append((a+i, b+j))

        for x in range(n):
            for y in range(n):
                if mat[x][y] == ' ':
                    num_regions += 1
                    dfs(x, y, num_regions)
        return num_regions


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [
    [[
        " /",
        "/ "
    ]],
    [[
        " /",
        "  "
    ]],
    [[
        "\\/",
        "/\\"
    ]],
    [[
        "/\\",
        "\\/"
    ]],
    [[
        "//",
        "/ "
    ]]
]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)



"""
* * 
 * *
  * 
   *


 * *
* * 
 * 
*      
"""