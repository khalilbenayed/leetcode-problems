"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

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

    Find nodes which have no incoming edges.
    """
    @staticmethod
    def run(n, edges):
        in_graph = defaultdict(list)
        for u, v in edges:
            in_graph[v].append(u)

        return [u for u in range(n) if u not in in_graph]


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    Same as above but different implementation
    """
    @staticmethod
    def run(n, edges):
        s = {v for _, v in edges}
        ans = []
        for v in range(n):
            if v not in s:
                ans.append(v)
        return ans


test_data = [[6, [[0,1],[0,2],[2,5],[3,4],[4,2]]], [5, [[0,1],[2,1],[3,1],[1,4],[2,4]]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
