"""
https://leetcode.com/problems/bricks-falling-when-hit/

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

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def restore_land(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                grid[i][j] = 1
            elif grid[i][j] == 1:
                grid[i][j] = 0


def find_land(grid, x, y):
    count, visited = 0, {(x, y)}
    if grid[x][y] == 1:
        stack = [(x, y)]
        while len(stack):
            i, j = stack.pop()
            grid[i][j] = 2
            for a, b in directions:
                if 0 <= i+a < len(grid) and 0 <= j+b < len(grid[0]) and grid[i+a][j+b] == 1 and (i+a, j+b) not in visited:
                    visited.add((i+a, j+b))
                    count += 1
                    stack.append((i+a, j+b))
    return count


def connected_to_roof(grid, x, y):
    if x == 0:
        return True
    for i, j in directions:
        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i + x][j + y] == 2:
            return True
    return False


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def hit_bricks(grid, hits):
        m, n = len(grid), len(grid[0])
        result = []
        for (x, y) in hits:
            grid[x][y] = 0
            for i in range(n):
                find_land(grid, 0, i)
            result.append(sum(sum(a for a in line if a == 1) for line in grid))
            restore_land(grid)
        return result


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    1) remove all hits
    2) mark all bricks connected to roof
    3) add hits in reverse order
        a) if connected to roof count how many were added, mark them
    """
    @staticmethod
    def hit_bricks(grid, hits):
        m, n = len(grid), len(grid[0])
        result = []
        hits_exists = [(x, y, grid[x][y]) for x, y in hits]
        # remove all hits
        for (x, y) in hits:
            grid[x][y] = 0
        # mark all bricks connected to roof
        for i in range(n):
            find_land(grid, 0, i)
        # add hits in reverse
        for (x, y, exists) in reversed(hits_exists):
            if not exists:
                result.append(0)
                continue
            grid[x][y] = 1
            if connected_to_roof(grid, x, y):
                res = find_land(grid, x, y)
                result.append(res)
            else:
                result.append(0)
        return list(reversed(result))


test_data = [[
    [[1, 0, 0, 0],
     [1, 1, 1, 0]],
    [[1, 0]]], [
    [[1, 0, 0, 0],
     [1, 1, 0, 0]],
    [[1, 1], [1, 0]]], [
    [[1, 0, 1],
     [1, 1, 1]],
    [[0, 0], [0, 2], [1, 1]]], [
    [[1], [1], [1], [1], [1]],
    [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]],[
    [[1, 1, 0],
     [0, 1, 0],
     [0, 0, 0]],
    [[0, 2], [2, 0], [0, 1], [1, 2]]], [
    [[1, 1, 0, 1, 0],
     [1, 1, 0, 1, 1],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]],
    [[5, 1], [1, 3]]
]
]
solutions = [Solution2.hit_bricks]
TestRunner.run(solutions, test_data)
