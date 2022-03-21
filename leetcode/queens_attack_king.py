"""
https://leetcode.com/problems/queens-that-can-attack-the-king/

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
    def run(queens, king):
        queens_set = set(list(map(lambda x: (x[0], x[1]), queens)))
        result = []

        # check king's row
        for i in range(king[0]+1, 8):
            if (i, king[1]) in queens_set:
                result.append((i, king[1]))
                break
        for i in reversed(range(king[0])):
            if (i, king[1]) in queens_set:
                result.append((i, king[1]))
                break

        # check king's column
        for i in range(king[1]+1, 8):
            if (king[0], i) in queens_set:
                result.append((king[0], i))
                break
        for i in reversed(range(king[1])):
            if (king[0], i) in queens_set:
                result.append((king[0], i))
                break

        # check king's diagonals
        for i in range(1, min(8-king[0], 8-king[1])):
            if (king[0]+i, king[1]+i) in queens_set:
                result.append((king[0]+i, king[1]+i))
                break
        for i in range(1, 1+min(king[0], king[1])):
            if (king[0]-i, king[1]-i) in queens_set:
                result.append((king[0]-i, king[1]-i))
                break

        for i in range(1, min(8-king[0], 1+king[1])):
            if (king[0]+i, king[1]-i) in queens_set:
                result.append((king[0]+i, king[1]-i))
                break
        for i in range(1, min(1+king[0], 8-king[1])):
            if (king[0]-i, king[1]+i) in queens_set:
                result.append((king[0]-i, king[1]+i))
                break

        return result


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [
    [[(0, 1), (1, 0), (4, 0), (0, 4), (3, 3), (2, 4)], (0, 0)],
    [[(0, 0), (1, 1), (2, 2), (3, 4), (3, 5), (4, 4), (4, 5)], (3, 3)],
    [[[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], (3, 4)]
]
solutions = [Solution1.run]
TestRunner.run(solutions, test_data)
