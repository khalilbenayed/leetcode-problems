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
        stack, parents = [root], {root.val: None}
        while len(stack) != 0:
            curr = stack.pop()
            if curr == target:
                break
            else:
                if curr.left:
                    stack.append(curr.left)
                    parents[curr.left.val] = curr
                if curr.right:
                    stack.append(curr.right)
                    parents[curr.right.val] = curr

        path = []
        endpoint = target
        while endpoint:
            path.append(endpoint)
            endpoint = parents[endpoint.val]

        def bfs(root, d):
            """Return children that are at distance d from root."""
            if d == 0:
                return [root.val]
            elif d > 0:
                ans = []
                if root.left:
                    ans.extend(bfs(root.left, d-1))
                if root.right:
                    ans.extend(bfs(root.right, d-1))
                return ans

        ans = []
        for i, node in enumerate(path):
            prev = path[i-1] if i > 0 else None
            if k-i == k:
                nodes = bfs(node, k)
                ans.extend(nodes)
            elif k-i > 0:
                if node.right == prev and node.left:
                    nodes = bfs(node.left, k-i-1)
                    ans.extend(nodes)
                elif node.left == prev and node.right:
                    nodes = bfs(node.right, k-i-1)
                    ans.extend(nodes)
            elif k-i == 0:
                ans.append(node.val)
            else:
                break
        return ans






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
