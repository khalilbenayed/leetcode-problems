"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
https://leetcode.com/problems/unique-binary-search-trees/

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


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(n):
        def generate_trees(n):
            def generate(start, end):
                if start == end:
                    return [None]
                if start + 1 == end:
                    return [TreeNode(start)]

                ans = []
                for i in range(start, end):
                    left_subtrees = generate(start, i)
                    right_subtrees = generate(i+1, end)
                    for left_subtree in left_subtrees:
                        for right_subtree in right_subtrees:
                            ans.append(TreeNode(i, left_subtree, right_subtree))
                return ans
            return generate(1, n+1)

        def num_trees_1(n):
            memo = {0: 1}
            def find(start, end):
                if end-start in memo:
                    return memo[end-start]

                ans = 0
                for i in range(start, end):
                    left_subtrees = find(start, i)
                    right_subtrees = find(i+1, end)
                    ans += left_subtrees * right_subtrees
                memo[end-start] = ans
                return ans
            return find(1, n+1)

        def num_trees_2(n):
            dp = [0] * (n + 1)
            dp[0] = 1

            for i in range(1, n+1):
                dp[i] = sum([dp[j] * dp[i-j-1] for j in range(i)])

            return dp[n]

        return num_trees_2(n)




class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[2], [3], [4]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
