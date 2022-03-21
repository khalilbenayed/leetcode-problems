"""
https://leetcode.com/problems/serialize-and-deserialize-bst/

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
    def __init__(self, x):
        pass


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """

    def serialize_recursive(self, root):
        """Encodes a tree to a single string."""
        def dfs(node):
            if node is not None:
                return '{node.val},{dfs(node.left)},{dfs(node.right)}'
            else:
                return '#'
        return dfs(root)

    def serialize_iterative(self, root):
        """Encodes a tree to a single string."""
        stack = [root]
        ids = []
        while len(stack) != 0:
            node = stack.pop()
            if node is None:
                ids.append('#')
            else:
                ids.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        return ','.join(ids)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        vals = data.split(',')
        def dfs(vals, index):
            if len(vals) > index and vals[index] != '#':
                root = TreeNode(vals[index])
                root.left, num_left_nodes = dfs(vals, index+1)
                root.right, num_right_nodes = dfs(vals, index+1+num_left_nodes)
                return root, num_left_nodes+num_right_nodes+1
            elif len(vals) > index:
                return None, 1
            else:
                return None, 0
        return dfs(vals, 0)[0]



class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass

