"""
https://leetcode.com/problems/interleaving-string/

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


class RecursiveMethod(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(s1, s2, s3):
        seen = set()

        def recurse(s, t, u):
            if len(s) == len(t) == len(u) == 0:
                return True
            res = False

            if len(s) > 0 and len(u) > 0 and s[0] == u[0] and (s[1:]+' '+t not in seen or t[1:]+' '+s not in seen):
                seen.add(s[1:]+' '+t)
                res |= recurse(s[1:], t, u[1:])
            if len(t) > 0 and len(u) > 0 and t[0] == u[0] and (s[1:]+' '+t not in seen or t[1:]+' '+s not in seen):
                seen.add(t[1:]+' '+s)
                res |= recurse(s, t[1:], u[1:])
            return res
        return recurse(s1, s2, s3)


test_data = [["aabcc", "dbbca", "aadbbcbcac"], ["aabcc", "dbbca", "aadbbbaccc"], ['a', '', 'a']]
solutions = [RecursiveMethod().run]
TestRunner.run(solutions, test_data)
