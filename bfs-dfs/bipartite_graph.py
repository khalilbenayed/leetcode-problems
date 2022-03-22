"""
https://leetcode.com/problems/is-graph-bipartite/

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

    BFS - Iterative
    """
    @staticmethod
    def run(graph):
        def isBipartite(graph) -> bool:
            n = len(graph)
            if n <= 2:
                return True
            colors = [None] * n
            for i in range(n):
                if colors[i] is not None:
                    continue
                stack = [(i, 0)]
                while len(stack) > 0:
                    u, color = stack.pop()
                    colors[u] = color
                    next_color = 0 if color == 1 else 1
                    for v in graph[u]:
                        if colors[v] is None:
                            stack.append((v, next_color))
                        elif colors[v] == color:
                            return False
            return True
        return isBipartite(graph)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    BFS Iterative
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[[[1,3], [0,2], [1,3], [0,2]]], [[[1,2,3], [0,2], [0,1,3], [0,2]]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
