"""
https://leetcode.com/problems/next-greater-node-in-linked-list/

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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    use a stack
    """
    @staticmethod
    def run(head):
        curr = head.next
        i = 1
        stack = [head.val]
        ans = []
        while curr:
            j = i
            while len(stack) != 0 and stack[-1] < curr.val:
                stack.pop()
                j -= 1
                ans[j] = curr.val
            stack.append(curr.val)
            ans.append(0)
            i += 1
        return ans


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    pretty much same as above, but maybe easier to understand?
    """
    @staticmethod
    def run(head):
        stack, ans = [], []
        curr, i = head, 0
        while curr is not None:
            while len(stack) != 0 and curr.val > stack[-1][0]:
                val, index = stack.pop()
                ans[index] = curr.val
            stack.append((curr.val, i))
            ans.append(0)
            i += 1
            curr = curr.next
        return ans


test_data = [[]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
