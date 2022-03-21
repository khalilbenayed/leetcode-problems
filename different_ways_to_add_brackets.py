"""
https://leetcode.com/problems/different-ways-to-add-parentheses/

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
    def run(input_string):
        # process the input string as array of terms and operators
        curr_str = ""
        expr = []
        for char in input_string:
            if "0" <= char <= "9":
                curr_str += char
            else:
                expr.extend([curr_str, char])
                curr_str = ""
        expr.append(curr_str)

        memo = {}

        def fn(expression):
            if len(expression) <= 1:
                return expression

            num_terms, num_operators = len(expression) // 2 + 1, len(expression) // 2

            possible_strings = []
            for term in range(0, num_terms-1):
                if ''.join(expression[:2*term+1]) not in memo:
                    memo[''.join(expression[:2*term+1])] = fn(expression[:2*term+1])
                left_strings = memo[''.join(expression[:2*term+1])]

                if ''.join(expression[2*(term+1):]) not in memo:
                    memo[''.join(expression[2*(term+1):])] = fn(expression[2*(term+1):])
                right_strings = memo[''.join(expression[2*(term+1):])]

                for left in left_strings:
                    for right in right_strings:
                        possible_string = "(" + left + ")" + expression[2*term+1] + "(" + right + ")"
                        possible_strings.append(possible_string)
            memo[''.join(expression)] = possible_strings
            return possible_strings

        return [eval(exp) for exp in fn(expr)]


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(input_string):
        pass


test_data = [["2-1-1"], ['2*3-4*5'], ["11"], ["0"]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
