"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

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

    First perform dfs to find path from root to target
    For every node on the path, add nodes that are k-n from node on the other branch to result set
        if the node is distance n away from target
    """
    @staticmethod
    def run(root, target, k):
        def fn(root, k):
            # gives the nodes that are k edges away from the root
            if root is None:
                return []

            if k == 0:
                return [root.val]

            result = []
            if root.left is not None:
                result.extend(fn(root.left, k - 1))
            if root.right is not None:
                result.extend(fn(root.right, k - 1))
            return result

        # now find path for the target from root
        stack = [[root]]
        path_to_target = None
        while len(stack) != 0:
            curr_path = stack.pop()
            if curr_path[-1] == target:
                path_to_target = curr_path
                break

            if curr_path[-1].left is not None:
                stack.append(curr_path + [curr_path[-1].left])
            if curr_path[-1].right is not None:
                stack.append(curr_path + [curr_path[-1].right])

        # now find the nodes k edges away from the target
        result = fn(target, k)
        n = len(path_to_target)
        for i in range(1, min(k + 1, n)):
            curr = path_to_target[n - i - 1]
            if k - i == 0:
                result.append(curr.val)
            else:
                # can't use the subtree the path follows
                next_in_path = path_to_target[n - i]
                if curr.left == next_in_path:
                    result.extend(fn(curr.right, k - i - 1))
                else:
                    result.extend(fn(curr.left, k - i - 1))
        return result


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
