"""
https://leetcode.com/problems/decode-string/

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


class RecursiveMethod(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    def decode(self, s):
        result = ''
        i = 0
        while i < len(s):
            factor_str = ''
            while i < len(s) and s[i] != '[':
                if '0' <= s[i] <= '9':
                    factor_str += s[i]
                else:
                    result += s[i]
                i += 1
            if i == len(s):
                break
            factor = int(factor_str)
            factor_str, i, state = '', i + 1, 0
            while i < len(s):
                if s[i] == '[':
                    factor_str += s[i]
                    state += 1
                elif s[i] == ']':
                    if state == 0:
                        i += 1
                        break
                    else:
                        factor_str += s[i]
                        state -= 1
                else:
                    factor_str += s[i]
                i += 1
            result += self.decode(factor_str) * factor
        return result


class IterativeMethod(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def decode(s):
        result = ''
        stack = [s]
        while len(stack) != 0:
            curr_s = stack.pop()
            factor_str, sub_str = '', ''
            i = 0
            while i < len(curr_s) and curr_s[i] != '[':
                if '0' <= curr_s[i] <= '9':
                    factor_str += curr_s[i]
                else:
                    result += curr_s[i]
                i += 1
            if i == len(curr_s):
                continue
            factor = int(factor_str)
            i, state = i + 1, 0
            while i < len(curr_s):
                if curr_s[i] == '[':
                    sub_str += curr_s[i]
                    state += 1
                elif curr_s[i] == ']':
                    if state == 0:
                        i += 1
                        break
                    else:
                        sub_str += curr_s[i]
                        state -= 1
                else:
                    sub_str += curr_s[i]
                i += 1
            if i != len(curr_s):
                stack.append(curr_s[i:])
            for _ in range(factor):
                stack.append(sub_str)
        return result


class OtherMethod(object):
    @staticmethod
    def decode(s):
        stack = []
        res = ''
        for c in s:
            if c == ']':
                curr_s, factor = '', ''
                while len(stack) and stack[-1] != '[':
                    curr_s = stack.pop() + curr_s
                stack.pop()
                while len(stack) and '0' <= stack[-1] <= '9':
                    factor = stack.pop() + factor
                curr_s *= int(factor)
                stack.append(curr_s)
            else:
                stack.append(c)
        while len(stack):
            res = stack.pop() + res
        return res


test_data = [['abc'], ['3[a]2[bc]'], ['3[a2[c]]'], ['2[abc]3[cd]ef']]
solutions = [RecursiveMethod().decode, IterativeMethod.decode, OtherMethod.decode]
TestRunner.run(solutions, test_data)
