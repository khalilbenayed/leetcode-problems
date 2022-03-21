"""
https://leetcode.com/problems/max-consecutive-ones-iii/

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

    it doesn't make sense to leave a hole in the middle
    -> find the indices of all zeros and slide through them
    -> for every 0 keep track of how many zeros before and after
    -> use this info to calculate max consecutive ones

    slow
    """
    @staticmethod
    def run(array, k):
        count, max_count = 0, 0
        for i in array:
            if i == 1:
                count += 1
            else:
                count = 0
            max_count = max(max_count, count)

        if k == 0:
            return max_count

        zeros, ones_count = [], 0
        for i, bit in enumerate(array):
            if bit == 1:
                ones_count += 1
                if i == len(array)-1:
                    zeros[-1]['after'] = ones_count
            else:
                if len(zeros) != 0:
                    zeros[-1]['after'] = ones_count
                zeros.append({'index': i, 'before': ones_count, 'after': 0})
                ones_count = 0
        if k >= len(zeros):
            return len(array)

        def max_consecutive_ones(flipped_zeros):
            return flipped_zeros[0]['before'] + \
                   flipped_zeros[-1]['index'] - flipped_zeros[0]['index'] + 1 + \
                   flipped_zeros[-1]['after']

        return max(max_consecutive_ones(zeros[i:i+k]) for i in range(len(zeros)-k+1))


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(array, k):
        zeros = max_count = left = 0
        for right, bit in enumerate(array):
            if bit == 0:
                zeros += 1
            while zeros > k:
                if array[left] == 0:
                    zeros -= 1
                left += 1
            max_count = max(max_count, right-left+1)
        return max_count


test_data = [[[1,1,1,0,0,0,1,1,1,1,0], 2], [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
