"""
https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/submissions/

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
    def run(favorite_companies):
        company_set_per_person = []
        for i, company_list in enumerate(favorite_companies):
            company_set = set(company_list)
            found = False
            for j, (other_company_set, k) in enumerate(company_set_per_person):
                if company_set >= other_company_set:
                    company_set_per_person[j] = (company_set, i)
                    found = True
                    break
                if company_set <= other_company_set:
                    found = True
                    break
            if not found:
                company_set_per_person.append((company_set, i))

        # print(company_set_per_person)

        ans = []
        for i, company_list in enumerate(favorite_companies):
            company_set = set(company_list)
            found = False
            for other_company_set, j in company_set_per_person:
                if company_set <= other_company_set and i != j:
                    found = True
                    break
            if not found:
                ans.append(i)
        return ans


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
