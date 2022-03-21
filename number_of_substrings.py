"""
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

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
    def run(s):
        found = {
            'a': 0,
            'b': 0,
            'c': 0
        }
        count, l, r = 0, 0, 0
        found[s[0]] = 1
        while l < len(s) - 2 and r < len(s):
            if 0 in found.values():
                if r == len(s) - 1:
                    break
                r += 1
                found[s[r]] += 1
            else:
                count += len(s) - r
                found[s[l]] -= 1
                l += 1
        return count


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(s):
        found = {
            'a': 0,
            'b': 0,
            'c': 0
        }
        count, l = 0, 0
        for r, c in enumerate(s):
            found[c] += 1
            while 0 not in found.values():
                count += len(s) - r
                found[s[l]] -= 1
                l += 1
        return count


test_data = [['abcabc'], ['aaacba'], ['acbbcac']]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
