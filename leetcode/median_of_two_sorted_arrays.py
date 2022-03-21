"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

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
    def run(nums1, nums2):
        def fn(nums1, nums2):
            n1, n2 = len(nums1), len(nums2)
            n = n1 + n2
            start, end = 0, n1
            mid1, mid2, median = None, None, None
            while start <= end:
                mid1 = min((end + start) // 2, (n + 1) // 2)
                mid2 = (n + 1) // 2 - mid1

                if mid2 > n2:
                    mid1 += mid2 - n2
                    mid2 = n2

                print(start, end, mid1, mid2, n1, n2)
                if mid1 < n1 and mid2 > 0 and nums2[mid2 - 1] > nums1[mid1]:
                    start = mid1 + 1
                elif mid1 > 0 and mid2 < n2 and nums1[mid1 - 1] > nums2[mid2]:
                    end = mid1
                else:
                    if mid1 <= 0:
                        median = nums2[mid2 - 1 + mid1]
                    elif mid2 <= 0:
                        median = nums1[mid1 - 1 + mid2]
                    else:
                        median = max(nums1[mid1 - 1], nums2[mid2 - 1])
                    break
            print(median)

            if n % 2 == 1:
                return median

            if mid1 == n1:
                return (median + nums2[mid2]) / 2
            if mid2 == n2:
                return (median + nums1[mid1]) / 2
            return (median + min(nums1[mid1], nums2[mid2])) / 2

        n1, n2 = len(nums1), len(nums2)
        if n1 == 0:
            return nums2[n2 // 2] if n2 % 2 == 1 else (nums2[n2 // 2 - 1] + nums2[n2 // 2]) / 2
        if n2 == 0:
            return nums1[n1 // 2] if n1 % 2 == 1 else (nums1[n1 // 2 - 1] + nums1[n1 // 2]) / 2
        if n1 < n2:
            return fn(nums2, nums1)
        return fn(nums1, nums2)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


"""
[1, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80] 40
[1, 20, 30, 40, 50, 60, 70, 80] 45, [10, 25, 75] 25

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16] 7
[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12, 14, 16]


"""

test_data = [[[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12, 14, 16]],
             [[6], [3, 4]], [[2], []], [[5], [1, 2, 3, 4, 6]],
             [[1, 2], [3, 4, 5, 6, 7, 8]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
