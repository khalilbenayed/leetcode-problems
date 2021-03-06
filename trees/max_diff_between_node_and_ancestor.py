"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

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
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    DFS: time limit exceeded
    """
    @staticmethod
    def run(root):
        def fn(node, ancestor=None):
            if node is None:
                return 0

            if ancestor is None:
                return max(fn(node.left, node), fn(node.right, node))

            return max(abs(ancestor.val - node.val),
                       fn(node.left, ancestor),
                       fn(node.left, node),
                       fn(node.right, ancestor),
                       fn(node.right, node))

        return fn(root)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    At every node, keep track of the min and max ancestors
    """
    @staticmethod
    def run(root):
        if root is None:
            return 0

        stack = [(root, None, None)]
        res = 0
        while len(stack) != 0:
            node, min_ancestor, max_ancestor = stack.pop()
            if min_ancestor is None:  # max_ancestor must also be none in this case
                if node.left is not None:
                    stack.append((node.left, node.val, node.val))
                if node.right is not None:
                    stack.append((node.right, node.val, node.val))
            else:
                res = max(res, abs(node.val - min_ancestor), abs(node.val - max_ancestor))
                min_ancestor = min(node.val, min_ancestor)
                max_ancestor = max(node.val, max_ancestor)
                if node.left is not None:
                    stack.append((node.left, min_ancestor, max_ancestor))
                if node.right is not None:
                    stack.append((node.right, min_ancestor, max_ancestor))
        return res


test_data = [[]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
