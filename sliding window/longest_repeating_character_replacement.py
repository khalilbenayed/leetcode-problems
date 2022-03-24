"""
https://leetcode.com/problems/longest-repeating-character-replacement/

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

    sliding window
    """
    @staticmethod
    def run(s, k):
        left, max_count = 0, 0
        dic = defaultdict(int)

        for right, char in enumerate(s):
            dic[char] += 1
            while right - left > max_count + k:
                dic[s[left]] -= 1
                left += 1
            max_count = max(max_count, dic[char])
            print(left, right, dic, max_count)
        return min(len(s), max_count + k)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(s, k):
        count = defaultdict(int)
        left, max_count = -1, 0
        for right, char in enumerate(s):
            count[char] += 1
            while right - left > max(count.values()) + k:
                left += 1
                count[s[left]] -= 1
            max_count = max(max_count, right-left)
        return max_count

test_data = [["ababb", 2], ["aababba", 1], ["abaa", 0]]
solutions = [Solution1.run]
TestRunner.run(solutions, test_data)
