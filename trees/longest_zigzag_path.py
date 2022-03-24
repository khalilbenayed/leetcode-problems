"""
https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

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
    """
    @staticmethod
    def run(root):
        def fn(node, curr_length=0, direction=None):
            if node is None:
                return curr_length

            if direction == 'left':
                max_length = max(fn(node.left, curr_length + 1, 'right'), fn(node.left)) if node.left is not None else curr_length
                if node.right is not None:
                    return max(max_length, fn(node.right, 1, 'left'), fn(node.right))
                return max_length

            elif direction == 'right':
                max_length = max(fn(node.right, curr_length + 1, 'left'), fn(node.right)) if node.right is not None else curr_length
                if node.left is not None:
                    return max(max_length, fn(node.left, 1, 'right'), fn(node.left))
                return max_length

            else:
                max_length = fn(node.left, 1, 'right') if node.left is not None else curr_length
                if node.right is not None:
                    return max(max_length, fn(node.right, 1, 'left'))
                return max_length
        return fn(root)


max_so_far = 0


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(root):
        def fn(node, direction):
            global max_so_far

            if node is None:
                return -1
            max_left = fn(node.left, 'right')
            max_right = fn(node.right, 'left')

            max_so_far = max(max_so_far, max_left + 1, max_right + 1)

            return 1 + (max_left if direction == 'left' else max_right)

        fn(root, 'left')
        return max_so_far


test_data = [[]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
