"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

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
    def run(nums, k):
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = (left+right) // 2
            print(left, right, mid)
            if nums[mid] == k:
                return mid
            if nums[left] == k:
                return left
            if nums[right] == k:
                return right
            if nums[left] <= nums[mid]:
                if nums[left] < k < nums[mid]:
                    print(11)
                    right = mid - 1
                else:
                    print(12)
                    left = mid + 1
            else:
                if nums[mid] < k < nums[left]:
                    print(21)
                    left = mid + 1
                else:
                    print(22)
                    right = mid - 1
        return -1


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(nums, k):
        def search(arr, l, h, key):
            if l > h:
                return -1

            mid = (l + h) // 2
            if arr[mid] == key:
                return mid

                # If arr[l...mid] is sorted
            if arr[l] <= arr[mid]:

                # As this subarray is sorted, we can quickly
                # check if key lies in half or other half
                if key >= arr[l] and key <= arr[mid]:
                    return search(arr, l, mid - 1, key)
                return search(arr, mid + 1, h, key)

                # If arr[l..mid] is not sorted, then arr[mid... r]
            # must be sorted
            if key >= arr[mid] and key <= arr[h]:
                return search(arr, mid + 1, h, key)
            return search(arr, l, mid - 1, key)
        return search(nums, 0, len(nums)-1, k)


test_data = [[[2,5,6,0,0,1,2], 0], [[1,3,1,1,1], 3]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
