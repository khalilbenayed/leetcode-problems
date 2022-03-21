"""
https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

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

    1) Compute prefix matrix (array of prefix array for each row)
    2) Compute prefix matrix column-wise
    2) use prefix to compute sum of square between each i, j pair
    """
    @staticmethod
    def run(mat, threshold):
        m, n = len(mat), len(mat[0])

        prefix = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]

        curr_max = 0
        for i in range(m+1):
            for j in range(n+1):
                start, end = 1, min(m-i, n-j)
                while start <= end:
                    mid = (start + end) // 2
                    curr_sum = prefix[i+mid][j+mid] - prefix[i+mid][j] - prefix[i][j+mid] + prefix[i][j]
                    if curr_sum > threshold:
                        end = mid-1
                    else:
                        curr_max = max(curr_max, mid)
                        start = mid + 1
        return curr_max


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [
    [[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4],
    [[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], 1],
    [[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 0],
    [[[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63,45]], 40184]
]

solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
