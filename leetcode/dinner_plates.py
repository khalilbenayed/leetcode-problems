"""
https://leetcode.com/problems/dinner-plate-stacks/

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


class DinnerPlates:
    """
    Use a stack for pushes and a stack for pops
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.left = self.right = 0

    def push(self, val):
        if len(self.stacks) == 0:
            self.stacks.append([val])
        else:
            while self.left < len(self.stacks) and len(self.stacks[self.left]) == self.capacity:
                self.left += 1

            if self.left == len(self.stacks):
                self.stacks.append([val])
            else:
                self.stacks[self.left].append(val)

        self.right = len(self.stacks) - 1

    def pop(self):
        if len(self.stacks) == 0:
            return -1

        while self.right >= 0 and len(self.stacks[self.right]) == 0:
            self.stacks.pop(self.right)
            self.right -= 1

        return self.stacks[self.right].pop() if self.right >= 0 else -1

    def pop_at_stack(self, index):
        if index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1

        if index < self.left:
            self.left = index
        return self.stacks[index].pop()


D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
D.pop_at_stack(0)
D.push(20)
D.push(21)
D.pop_at_stack(0)
D.pop_at_stack(2)
D.pop()
D.pop()
D.pop()
D.pop()
D.pop()
