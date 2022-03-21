"""
https://leetcode.com/problems/merge-k-sorted-lists/

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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Record:
    def __init__(self, node):
        self.val = node.val
        self.node = node

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(lists):
        curr_heap = [Record(head) for head in lists]
        heapq.heapify(curr_heap)
        head = curr = None
        while len(curr_heap) != 0:
            record = heapq.heappop(curr_heap)
            val, node = record.val, record.node
            new_node = ListNode(val)
            if curr is None:
                head = curr = new_node
            else:
                curr.next = new_node
                curr = new_node
            if node.next is not None:
                heapq.heappush(curr_heap, Record(node.next))
        return head


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(lists):
        nums = {}
        for curr in lists:
            while curr is not None:
                if curr.val in nums:
                    nums[curr.val] += 1
                else:
                    nums[curr.val] = 1
        head = curr = None
        for val in range(-10000, 10001):
            if val in nums:
                count = nums[val]
                for _ in range(count):
                    new_node = ListNode(val)
                    if curr is None:
                        head = curr = new_node
                    else:
                        curr.next = new_node
                        curr = new_node
        return head


test_data = [[]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
