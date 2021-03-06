"""
https://leetcode.com/problems/loud-and-rich/

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

    DP:
        - first construct directed graph of richness: u -> v means v is richer than u
        - use cache to store results for each vertex
        - for each vertex, result is min out of every neighbour
    """
    @staticmethod
    def run(richer, quiet):
        graph = defaultdict(list)
        for u, v in richer:
            graph[v].append(u)

        dp = {}

        def fn(x):
            # returns answer for node x
            if len(graph[x]) == 0:
                return x

            if x in dp:
                return dp[x]

            ans = x
            for neighbour in graph[x]:
                candidate = fn(neighbour)
                if quiet[candidate] < quiet[ans]:
                    ans = candidate

            dp[x] = ans
            return ans

        return [fn(x) for x in range(len(quiet))]


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[[[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
