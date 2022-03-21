"""
https://leetcode.com/problems/implement-stack-using-queues/

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
from collections import deque
from test_runner import TestRunner


class MyStack:
    def __init__(self):
        """Initialize your data structure here."""
        self.queue_2 = deque([])
        self.queue_1 = deque([])

    def push(self, x):
        """Push element x onto stack."""
        if len(self.queue_1) != 0 or len(self.queue_2) == 0:
            self.queue_1.appendleft(x)
        else:
            self.queue_2.appendleft(x)

    def pop(self):
        """Removes the element on top of the stack and returns that element."""
        if len(self.queue_1)  != 0:
            while len(self.queue_1) != 1:
                self.queue_2.appendleft(self.queue_1.pop())
            return self.queue_1.pop()
        elif len(self.queue_2)  != 0:
            while len(self.queue_2) != 1:
                self.queue_1.appendleft(self.queue_2.pop())
            return self.queue_2.pop()
        else:
            raise Exception('Should not be here.')

    def top(self):
        """Get the top element."""
        if len(self.queue_1)  != 0:
            while len(self.queue_1) != 1:
                self.queue_2.appendleft(self.queue_1.pop())
            val = self.queue_1.pop()
            self.queue_2.appendleft(val)
        elif len(self.queue_2)  != 0:
            while len(self.queue_2) != 1:
                self.queue_1.appendleft(self.queue_2.pop())
            val = self.queue_2.pop()
            self.queue_1.appendleft(val)
        else:
            raise Exception('Should not be here.')
        return val

    def empty(self):
        """Returns whether the stack is empty."""
        return len(self.queue_1) == len(self.queue_2) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())

stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack.empty())
