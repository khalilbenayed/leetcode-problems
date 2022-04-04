"""
https://leetcode.com/problems/sum-of-distances-in-tree/

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

from collections import defaultdict
from test_runner import TestRunner


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    DFS return the sum of distances of all nodes that are reachable without going through the source
    """
    @staticmethod
    def run(n, edges):
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        mem = {}

        def dfs(u, source=None):
            # return the sum of distances from u as root without going through source
            # also return number of nodes reachable
            if (u, source) in mem:
                return mem[(u, source)]

            distances, nodes_reached = 0, 1
            for v in tree[u]:
                if source is None or v != source:
                    distances1, nodes_reached1 = dfs(v, u)
                    distances += distances1 + nodes_reached1
                    nodes_reached += nodes_reached1
            mem[(u, source)] = (distances, nodes_reached)
            return distances, nodes_reached

        return [dfs(u)[0] for u in range(n)]


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(n, edges):
        # first process the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # root the tree at 0 and run dfs with memo
        counts, sums = [1] * n, [0] * n

        def dfs_1(u, source=None):
            for v in graph[u]:
                if source is None or v != source:
                    dfs_1(v, u)
                    counts[u] += counts[v]
                    sums[u] += sums[v] + counts[v]

        dfs_1(0)
        # counts are correct, sums[0] only is correct
        # now need to fix all other sums

        def dfs_2(u, source=None):
            if source is not None:
                sums[u] = sums[source] + n - 2 * counts[u]
            for v in graph[u]:
                if source is None or v != source:
                    dfs_2(v, u)
        dfs_2(0)

        return sums


test_data = [[6, [[0,1],[0,2],[2,3],[2,4],[2,5]]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
