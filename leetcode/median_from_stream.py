"""
https://leetcode.com/problems/find-median-from-data-stream/

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


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.first_half, self.second_half = [], []

    def add_num(self, num):
        if len(self.first_half) == len(self.second_half) == 0:
            heapq.heappush(self.first_half, -num)
            return
        median = self.find_median()
        if num <= median:
            heapq.heappush(self.first_half, -num)
            if abs(len(self.first_half)-len(self.second_half)) > 1:
                heapq.heappush(self.second_half, -heapq.heappop(self.first_half))
        if num > median:
            heapq.heappush(self.second_half, num)
            if abs(len(self.first_half)-len(self.second_half)) > 1:
                heapq.heappush(self.first_half, -heapq.heappop(self.second_half))

    def find_median(self):
        if len(self.first_half) == len(self.second_half):
            return (self.second_half[0]-self.first_half[0]) / 2
        elif len(self.first_half) > len(self.second_half):
            return -self.first_half[0]
        else:
            return self.second_half[0]


obj = MedianFinder()
obj.add_num(1)
print(obj.find_median())
obj.add_num(2)
print(obj.find_median())
obj.add_num(3)
print(obj.find_median())
