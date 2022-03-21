"""
https://leetcode.com/problems/get-the-maximum-score/

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
from collections import defaultdict


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        ans = sum1 = sum2 = 0
        i, j = n1-1, n2-1
        while i >= 0 and j >= 0:
            print(i, j, sum1, sum2, ans)
            if nums1[i] > nums2[j]:
                sum1 += nums1[i]
                i -= 1
            elif nums2[j] > nums1[i]:
                sum2 += nums2[j]
                j -= 1
            else:  # nums1[i] == nums2[j]
                ans += max(sum1 + nums1[i], sum2 + nums2[j])
                sum1 = sum2 = 0
                i -= 1
                j -= 1
        if i >= 0:
            ans += max(sum1 + sum(nums1[:i+1]), sum2)
        if j >= 0:
            ans += max(sum1, sum2 + sum(nums2[:j+1]))
        return ans


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[[2,4,5,8,10], [4,6,8,9]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)




"""
[7, 7, 0],
[-4, -7, 7],
[-4, 0, -2],
[-8, -5, 6]

[7, 14, 14],
[3, 3, 10],
[-1, -1, 4],
[-9, -14, -3]

[1,0,2,2]
"""