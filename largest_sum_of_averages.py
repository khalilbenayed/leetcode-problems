"""
https://leetcode.com/problems/largest-sum-of-averages/

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
    def run(A, K):
        memo = {}

        def fn(nums, k):
            if len(nums) <= k:
                return sum(nums)
            elif k == 1:
                return sum(nums) / len(nums)
            else:
                max_avg = 0
                for i in reversed(range(len(nums))):
                    key = (tuple([num for num in nums[:i]]), k-1)
                    if key not in memo:
                        memo[key] = fn([num for num in nums[:i]], k-1)
                    avg = memo[key] + sum(nums[i:]) / (len(nums) - i)
                    max_avg = max(max_avg, avg)
                return max_avg

        return fn(A, K)





class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    dp[i][k] = largest avg sum of 0...i with k elements
    """
    @staticmethod
    def run(A, K):
        n = len(A)
        dp = [[0] * K for _ in range(n)]
        dp[0][0] = A[0]
        for i in range(1, n):
            dp[i][0] = (dp[i-1][0] * i + A[i]) / (i + 1)

        for k in range(1, K):
            for i in range(k, n):
                curr_sum = 0
                for j in reversed(range(k, i+1)):
                    curr_sum += A[j]
                    dp[i][k] = max(dp[i][k], dp[j-1][k-1] + curr_sum / (i+1 - j))
        return dp[n-1][K-1]


test_data = [[[9, 1, 2, 3, 9], 3]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
