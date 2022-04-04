"""
https://leetcode.com/problems/path-with-maximum-probability/

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
import heapq
from collections import defaultdict
from test_runner import TestRunner


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    A* search
    """
    @staticmethod
    def run(n, edges, probs, s, t):
        graph = defaultdict(dict)
        for i, (u, v) in enumerate(edges):
            graph[u][v] = probs[i]
            graph[v][u] = probs[i]

        frontier = [(-1, s)]
        seen = set()
        while len(frontier) != 0:
            neg_prob, u = heapq.heappop(frontier)

            if u == t:
                return -neg_prob

            if u in seen:
                continue

            seen.add(u)
            for v, prob in graph[u].items():
                if v not in seen:
                    heapq.heappush(frontier, (neg_prob * prob, v))
        return 0


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(n, edges, probs, s, t):
        pass


test_data = [[3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2],
             [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2],
             [3, [[0,1]], [0.5], 0, 2],
             [5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
