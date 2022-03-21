"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

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
import heapq
from test_runner import TestRunner


class Solution3(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    greedy: sort the lists using the last element

    -> smallest last element is left limit of the range, now need to find the right limit
    -> use binary search

    does not work because we want the smallest numbers of the smallest range
      this gives largest numbers of smallest range
    """
    @staticmethod
    def run(nums):
        nums = sorted(nums, key=lambda lst: lst[-1])
        right_limit = left_limit = nums[0][-1]

        def binary_search_for_next(lst, k):
            start, end = 0, len(lst) - 1
            while start <= end:
                mid = (start + end) // 2
                if lst[mid] == k:
                    return k
                if lst[mid] < k:
                    start = mid + 1
                else:
                    end = mid - 1
            return lst[start]

        for lst in nums:
            right_limit = max(right_limit, binary_search_for_next(lst, left_limit))

        return [left_limit, right_limit]


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(nums):
        nums_next = [(lst[0], 0, i) for i, lst in enumerate(nums)]
        best_left, best_right = None, None
        while True:
            left, left_index, i = min(nums_next, key=lambda x: x[0])
            right = max(nums_next, key=lambda x: x[0])[0]

            if best_left is None:
                best_left, best_right = left, right
            else:
                if right - left < best_right - best_left:
                    best_left, best_right = left, right
            if left_index == len(nums[i]) - 1:
                break
            nums_next[i] = (nums[i][left_index+1], left_index + 1, i)
        return [best_left, best_right]


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """

    @staticmethod
    def run(nums):
        nums_next = [(lst[0], 0, i) for i, lst in enumerate(nums)]
        max_num = max(nums_next, key=lambda x: x[0])[0]
        heapq.heapify(nums_next)
        best_left = best_right = None
        while True:
            left, left_index, i = heapq.heappop(nums_next)
            right = max_num

            if best_left is None:
                best_left, best_right = left, right
            else:
                if right - left < best_right - best_left:
                    best_left, best_right = left, right
            if left_index == len(nums[i]) - 1:
                break
            heapq.heappush(nums_next, (nums[i][left_index+1], left_index + 1, i))
            max_num = max(max_num, nums[i][left_index+1])

        return [best_left, best_right]


test_data = [[[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]], [[[1,2,3],[1,2,3],[1,2,3]]], [[[10,10],[11,11]]], [[[10],[11]]], [[[1],[2],[3],[4],[5],[6],[7]]]]
solutions = [Solution1.run, Solution2.run, Solution3.run]
TestRunner.run(solutions, test_data)
