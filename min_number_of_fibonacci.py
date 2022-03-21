"""
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

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

    1) compute all fibonacci <= k
    2) in a map, save all possible sums (if already exists, choose the one with minimum # terms)
    -> not fast enough

    1) compute largest fibonacci <= k: F[x]
    2) return 1 + recurse(k-F[x])
    """
    @staticmethod
    def run(k):
        def fn(k):
            fibonacci = [1, 1]
            while fibonacci[-1] < k:
                next_fibonacci = fibonacci[0] + fibonacci[1]
                fibonacci[0], fibonacci[1] = fibonacci[1], next_fibonacci
            if fibonacci[1] == k:
                return 1
            return 1 + fn(k-fibonacci[0])
        return fn(k)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    same as above but iterative
    """
    @staticmethod
    def run(k):
        fibonacci = [1, 1]
        while fibonacci[-1] < k:
            next_fibonacci = fibonacci[-2] + fibonacci[-1]
            fibonacci.append(next_fibonacci)
        i, count = len(fibonacci)-1, 0
        while k != 0:
            while fibonacci[i] > k:
                i -= 1
            k -= fibonacci[i]
            count += 1
        return count


test_data = [[7], [10], [19], [9083494]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
