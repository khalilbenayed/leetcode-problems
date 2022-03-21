"""
https://leetcode.com/problems/minimum-genetic-mutation/

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
    def run(start, end, bank):
        def are_neighbours(g1, g2):
            return sum(c1 != c2 for c1, c2 in zip(g1, g2)) == 1

        bank = [start] + bank

        # first build graph from the bank
        graph = {gene: [] for gene in bank}
        for i, g1 in enumerate(bank):
            for j in range(i+1, len(bank)):
                g2 = bank[j]
                if are_neighbours(g1, g2):
                    graph[g1].append(g2)
                    graph[g2].append(g1)

        # now perform bfs from start until end is found
        queue = deque([(start, 0)])
        seen = set()
        while len(queue) != 0:
            curr_gene, step = queue.popleft()
            if curr_gene == end:
                return step
            seen.add(curr_gene)
            for next_gene in graph[curr_gene]:
                if next_gene not in seen:
                    queue.append((next_gene, step + 1))

        return -1


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [["AACCGGTT", "AACCGGTA", ["AACCGGTA"]],
             ["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]],
             ["AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]]]
solutions = [Solution1.run]
TestRunner.run(solutions, test_data)
