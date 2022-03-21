"""
https://leetcode.com/problems/n-queens/

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

    CSP implementation:
    * A state k: The assignment of rows for each of the k leftmost queens
    * Initial state: No queens assigned
    * Goal state: All queens assigned with no pairs of queens attacking each other
    * Successor function: Add a queens to the leftmost columns in a valid row
    """
    @staticmethod
    def run(n):
        init_state = []

        def is_valid(state, x_j):
            j = len(state)
            for i, x_i in enumerate(state):
                if x_i == x_j or abs(x_i - x_j) == abs(i - j):
                    return False
            return True

        def get_successors(state):
            k = len(state)
            successors = []
            for x_j in range(n):
                if is_valid(state, x_j):
                    successors.append(state + [x_j])
            return successors

        def get_board(state):
            board = [["."] * n for _ in range(n)]
            for i, x_i in enumerate(state):
                board[i][x_i] = 'Q'
            for i, row in enumerate(board):
                board[i] = "".join(row)
            return board

        stack = [init_state]
        ans = []
        while len(stack) != 0:
            state = stack.pop()
            if len(state) == n:
                ans.append(get_board(state))
                continue
            successors = get_successors(state)
            for successor in successors:
                stack.append(successor)

        return ans


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(*args):
        pass


test_data = [[4], [1]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
