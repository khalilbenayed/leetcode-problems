"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

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
from collections import deque
from test_runner import TestRunner


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    Apply bfs from left to right and connect nodes in the same level
    """
    @staticmethod
    def run(root):
        if root is None:
            return root

        queue = deque([(root, 0)])
        curr_level, prev = 0, None
        while len(queue) != 0:
            curr, level = queue.popleft()
            if level == curr_level and prev is not None:
                prev.next = curr

            curr_level, prev = level, curr
            if curr.left:
                queue.append((curr.left, level+1))
            if curr.right:
                queue.append((curr.right, level+1))

        return root


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    Fill next pointers level by level and use it to iterate over the tree
    """
    @staticmethod
    def run(root):
        next_level_first, next_level_last = None, None
        curr = root
        curr.next = None

        while curr is not None:
            if next_level_first is None:
                if curr.left:
                    next_level_first = next_level_last = curr.left
                    if curr.right:
                        next_level_last.next = curr.right
                        next_level_last = curr.right
                elif curr.right:
                    next_level_first = next_level_last = curr.right
            else:
                if curr.left:
                    next_level_last.next = curr.left
                    next_level_last = curr.left
                if curr.right:
                    next_level_last.next = curr.right
                    next_level_last = curr.right

            if curr.next is not None:
                curr = curr.next
            else:
                curr = next_level_first
                next_level_first, next_level_last = None, None
        return root

        



test_data = [[]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
