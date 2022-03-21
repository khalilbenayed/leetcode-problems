"""
https://leetcode.com/problems/verifying-an-alien-dictionary/

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
    """
    @staticmethod
    def run(words, order):
        alphabet_order = {}
        for i, letter in enumerate(order):
            alphabet_order[letter] = i

        def compare(w1, w2):
            if len(w1) > len(w2) and w1.startswith(w2):
                return False

            l = min(len(w1), len(w2))
            for i in range(l):
                if alphabet_order[w1[i]] < alphabet_order[w2[i]]:
                    return True
                if alphabet_order[w1[i]] > alphabet_order[w2[i]]:
                    return False
            return True

        for i in range(len(words)-1):
            if not compare(words[i], words[i+1]):
                return False
        return True

class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [
    [['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'],
    [['word', 'world', 'row'], "worldabcefghijkmnpqstuvxyz"]
]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
