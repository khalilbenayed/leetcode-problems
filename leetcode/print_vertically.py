"""
https://leetcode.com/problems/print-words-vertically/

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
        words = s.split(' ')
        max_length = reduce(lambda y, x: max(y, len(x)), words, 0)
        result = [""] * max_length
        line_lengths = [-1] * max_length
        for i, word in enumerate(reversed(words)):
            for line in range(len(word)):
                if line_lengths[line] == -1:
                    line_lengths[line] = len(words)-i
        print(line_lengths)

        for i in range(max_length):
            for word in words:
                if i < len(word):
                    result[i] += word[i]
                elif len(result[i]) < line_lengths[i]:
                    result[i] += ' '
        return result


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [["HOW ARE YOU"], ["TO BE OR NOT TO BE"], ["CONTEST IS COMING"]]
solutions = [Solution1.run]
TestRunner.run(solutions, test_data)


"""
z xxx y aaaa bbb c

zxyabc
 x ab
 x ab
   a
"""
