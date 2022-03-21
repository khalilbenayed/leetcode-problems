"""
https://leetcode.com/problems/course-schedule-ii/

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
    def run(n, prereqs):
        result, done = [], set()
        prereqs_dict = {i: set() for i in range(n)}
        for c, p in prereqs:
            prereqs_dict[c].add(p)
        while len(result) != n:
            # print(result, done, prereqs_dict)
            found = False
            for c, p in prereqs_dict.items():
                if len(p) == 0:
                    found = True
                    result.append(c)
                    done.add(c)
            for c, p in prereqs_dict.items():
                prereqs_dict[c] = prereqs_dict[c] - done
            if not found:
                return []
            prereqs_dict = {key: value for key, value in prereqs_dict.items() if key not in done}
        return result


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[2, [[1, 0]]], [4, [[1, 0], [2, 0], [3, 1], [3, 2]]], [2, [[0, 1]]]]
solutions = [Solution1.run]
TestRunner.run(solutions, test_data)
