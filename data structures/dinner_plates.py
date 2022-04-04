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
import heapq

class DinnerPlates:
    """
    Use a stack for pushes and a stack for pops
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.stacks_not_full = []  # heap of stacks not full (minheap)
        self.stacks_not_empty = []  # heap of stacks not empty (maxheap)

    def push(self, val: int) -> None:
        if len(self.stacks_not_full) != 0:
            index = self.stacks_not_full[0]
            self.stacks[index].append(val)

            if len(self.stacks[index]) == self.capacity:
                heapq.heappop(self.stacks_not_full)

            if len(self.stacks[index]) == 1:
                heapq.heappush(self.stacks_not_empty, -index)
        else:
            index = len(self.stacks)
            self.stacks.append([val])
            if self.capacity > 1:
                heapq.heappush(self.stacks_not_full, index)
            heapq.heappush(self.stacks_not_empty, -index)

    def pop(self) -> int:
        if len(self.stacks_not_empty) == 0:
            return -1

        neg_index = self.stacks_not_empty[0]
        while len(self.stacks[-neg_index]) == 0:
            heapq.heappop(self.stacks_not_empty)
            neg_index = self.stacks_not_empty[0]

        val = self.stacks[-neg_index].pop()

        # update self.stacks_not_empty
        if len(self.stacks[-neg_index]) == 0:
            heapq.heappop(self.stacks_not_empty)

        # update self.stacks_not_full
        if len(self.stacks[-neg_index]) == self.capacity - 1:
            heapq.heappush(self.stacks_not_full, -neg_index)
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1

        val = self.stacks[index].pop()

        # update self.stacks_not_full
        if len(self.stacks[index]) == self.capacity - 1:
            heapq.heappush(self.stacks_not_full, index)
        return val


D = DinnerPlates(2)
D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)
D.popAtStack(0)
D.push(20)
D.push(21)
D.popAtStack(0)
D.popAtStack(2)
D.pop()
D.pop()
D.pop()
D.pop()
D.pop()
