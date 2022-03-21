"""
https://leetcode.com/problems/sliding-window-median/

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
from sortedcontainers import SortedList
from test_runner import TestRunner


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(nums, k):
        n = len(nums)
        first_half, second_half = [], []

        def find_median():
            if len(first_half) == len(second_half):
                return (second_half[0] - first_half[0]) / 2
            if len(first_half) == len(second_half) + 1:
                return -first_half[0]
            if len(second_half) == len(first_half) + 1:
                return second_half[0]
            raise Exception('Should not be here')

        def add(num):
            if len(first_half) == len(second_half):
                if len(first_half) == 0 or num <= second_half[0]:
                    heapq.heappush(first_half, -num)
                else:
                    heapq.heappush(second_half, num)
            elif len(first_half) == len(second_half) + 1:
                if num < -first_half[0]:
                    heapq.heappush(second_half, -heapq.heappop(first_half))
                    heapq.heappush(first_half, -num)
                else:
                    heapq.heappush(second_half, num)
            elif len(second_half) == len(first_half) + 1:
                if num > second_half[0]:
                    heapq.heappush(first_half, -heapq.heappop(second_half))
                    heapq.heappush(second_half, num)
                else:
                    heapq.heappush(first_half, -num)
            else:
                raise Exception('Should not be here')

        def remove(num):
            if len(first_half) == len(second_half):
                if num <= -first_half[0]:
                    index = first_half.index(-num)
                    first_half[index] = first_half[-1]
                    first_half.pop()
                    heapq.heapify(first_half)
                else:
                    index = second_half.index(num)
                    second_half[index] = second_half[-1]
                    second_half.pop()
                    heapq.heapify(second_half)
            elif len(first_half) == len(second_half) + 1:
                if num <= -first_half[0]:
                    index = first_half.index(-num)
                    first_half[index] = first_half[-1]
                    first_half.pop()
                    heapq.heapify(first_half)
                else:
                    index = second_half.index(num)
                    second_half[index] = -heapq.heappop(first_half)
                    heapq.heapify(second_half)
            elif len(second_half) == len(first_half) + 1:
                if num >= second_half[0]:
                    index = second_half.index(num)
                    second_half[index] = second_half[-1]
                    second_half.pop()
                    heapq.heapify(second_half)
                else:
                    index = first_half.index(-num)
                    first_half[index] = -heapq.heappop(second_half)
                    heapq.heapify(first_half)
            else:
                raise Exception('Should not be here')

        # start reading first k nums and fill up heaps to find median
        for i in range(k):
            add(nums[i])

        medians = []

        # now start sliding the window
        for i in range(n-k):
            medians.append(find_median())
            remove(nums[i])
            add(nums[i+k])
        medians.append(find_median())

        return medians


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(nums, k):
        odd = k % 2 == 1  # there are odd numbers of items in the window

        lst = SortedList()  # maintain a sorted list

        res = []
        for num in nums[:k]:  # put the first k items in the SortedList
            lst.add(num)
        median = lst[k // 2] if odd else (lst[k // 2 - 1] + lst[k // 2]) / 2
        res.append(median)

        i = k
        while i < len(nums):
            lst.remove(nums[i - k])  # if we use heapq here, it takes O(k) here, but for sortedList, it takes O(logk)
            lst.add(nums[i])
            median = lst[k // 2] if odd else (lst[k // 2 - 1] + lst[k // 2]) / 2
            res.append(median)
            i += 1

        return res


test_data = [[[1,3,-1,-3,5,3,6,7], 3], [[1,2], 1]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
