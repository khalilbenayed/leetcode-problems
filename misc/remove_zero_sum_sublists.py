"""
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

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
    def run(head):
        cur = head
        m = {}
        s = 0
        while cur is not None:
            s += cur.val
            if s == 0:
                head = cur.next
                m = {}
            elif s in m:
                temp = m[s].next
                temp_sum = s
                while temp != cur:
                    temp_sum += temp.val
                    del m[temp_sum]
                    temp = temp.next
                m[s].next = cur.next
            else:
                m[s] = cur
            cur = cur.next
        return head


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
