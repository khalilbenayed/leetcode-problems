"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/

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
    """
    @staticmethod
    def run(root):
        if root is None:
            return True

        queue = deque([(root, 0)])
        curr_level, prev_count, curr_count = 0, None, 0
        last_right_is_null = False
        while len(queue) != 0:
            curr, level = queue.popleft()
            if level > curr_level:
                if prev_count is not None and prev_count * 2 != curr_count:
                    return False
                curr_level, prev_count, curr_count = level, curr_count, 1
            else:
                if last_right_is_null and curr.left is not None:
                    return False
                curr_count += 1

            if curr.left is not None:
                queue.append((curr.left, level + 1))
            if curr.right is not None:
                if curr.left is None:
                    return False
                queue.append((curr.right, level + 1))
                last_right_is_null = False
            else:
                last_right_is_null = True

        return True


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(root):
        def fn(root):
            if root.left is None and root.right is None:
                return True, 1, True

            if root.left is None and root.right is not None:
                return False, 0, False

            left_is_complete, left_height, left_is_full = fn(root.left)
            if root.right is None:
                return left_is_complete and left_height == 1, 1 + left_height, False
            else:
                right_is_complete, right_height, right_is_full = fn(root.right)
                if right_height == left_height:
                    return left_is_full and right_is_complete, 1 + left_height, left_is_full and right_is_full
                elif right_height == left_height - 1:
                    return left_is_complete and right_is_full, 1 + left_height, False
                else:
                    return False, 0, False

        if root is None:
            return True
        return fn(root)[0]


test_data = [[]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
