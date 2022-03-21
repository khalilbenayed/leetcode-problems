"""
https://leetcode.com/problems/valid-parenthesis-string/

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
    def run(string):
        n = len(string)
        dp = [[None] * (n+1) for _ in range(n+1)]

        def fn(start, balance):
            if balance < 0:
                return False

            if start == n:
                return balance == 0

            for i in range(start, n):
                char = string[i]
                if char == "(":
                    balance += 1
                elif char == ")" and balance > 0:
                    balance -= 1
                elif char == ")":  # balance <= 0
                    return False
                else:
                    if dp[i + 1][balance] is None:
                        dp[i + 1][balance] = fn(i+1, balance)

                    if dp[i + 1][balance + 1] is None:
                        dp[i + 1][balance + 1] = fn(i+1, balance+1)

                    if dp[i + 1][balance - 1] is None:
                        dp[i + 1][balance - 1] = fn(i+1, balance-1)

                    return dp[i+1][balance] or dp[i+1][balance+1] or dp[i+1][balance-1]

            return balance == 0
        return fn(0, 0)


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(string):
        max_open, extra_close = 0, 0
        for char in string:
            if char == "(":
                max_open += 1
                extra_close += 1
            elif char == ")":
                max_open -= 1
                extra_close = max(extra_close - 1, 0)
            else:
                max_open += 1
                extra_close = max(extra_close - 1, 0)

            if max_open < 0:
                return False
        return extra_close == 0


test_data = [["()"], ["(*)"], ["(*"], ["(*))"], ["(*)))"], [")("], ["(((**)))"], ["(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
