"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    def run(inorder, postorder):
        def fn(inorder, postorder):
            if len(inorder) == len(postorder) == 0:
                return None

            root_val = postorder[-1]
            root_index = inorder.index(root_val)

            inorder_left, inorder_right = inorder[:root_index], inorder[root_index+1:]
            postorder_left, postorder_right = postorder[:root_index], postorder[root_index:-1]

            left_subtree = fn(inorder_left, postorder_left)
            right_subtree = fn(inorder_right, postorder_right)

            return TreeNode(root_val, left_subtree, right_subtree)

        return fn(inorder, postorder)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[[9,3,15,20,7], [9,15,7,20,3]], [[2,1], [2,1]], [[1, 2, 3], [3, 2, 1]]]
solutions = [Solution1.run]
TestRunner.run(solutions, test_data)
