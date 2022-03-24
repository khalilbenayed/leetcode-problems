"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?fbclid=IwAR0ChuUeNk_ZxjUzWAPBmZeazDlQELSn6PzN_T8VboHG9Ggw0juBBim4QWY

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
    1) run dfs
    2) when find p or q save the path from root
    3) select min from intersection
    """
    @staticmethod
    def find_lca(root, p, q):
        # find paths for p and q
        stack = [[root]]
        path_to_p, path_to_q = None, None
        while len(stack) != 0:
            path = stack.pop()
            if path[-1] == p:
                path_to_p = path

            if path[-1] == q:
                path_to_q = path

            if path_to_p is not None and path_to_q is not None:
                break

            if path[-1].left is not None:
                stack.append(path + [path[-1].left])

            if path[-1].right is not None:
                stack.append(path + [path[-1].right])

        # now find where the paths diverge
        i = 0
        while i < min(len(path_to_p), len(path_to_q)) and path_to_p[i] == path_to_q[i]:
            i += 1
        return path_to_p[i - 1]


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    Same as above but optimized
    """
    @staticmethod
    def run(root, p, q):
        p_path, q_path, path, visited = [], [], [], set()
        stack = [root]
        while len(stack):
            cur = stack.pop()
            path.append(cur)
            if cur == p:
                p_path = [v for v in path]
            if cur == q:
                q_path = [v for v in path]
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            while len(path):
                cur = path[-1]
                if (cur.left is None or cur.left in visited) and (cur.right is None or cur.right in visited):
                    visited.add(cur)
                    path.pop()
                else:
                    break
        i = 0
        while i < min(len(p_path), len(q_path)) and p_path[i] == q_path[i]:
            i += 1
        return p_path[i-1]

test_data = [[]]
solutions = [Solution1.find_lca, Solution2.run]
TestRunner.run(solutions, test_data)
