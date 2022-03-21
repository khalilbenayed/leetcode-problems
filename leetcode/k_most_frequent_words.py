"""
https://leetcode.com/problems/top-k-frequent-words/?fbclid=IwAR0ZRR05ElBmN3zjhpu31jHq9rxDU0lUrH6LphjmVscsLqi3Bb52DrT7efU

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
from collections import Counter
import heapq
from test_runner import TestRunner


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    uses max heap -> O(nlogn)
    """
    @staticmethod
    def run(words, k):
        counter = Counter(words)
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, (-freq, word))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result


class Word:
    def __init__(self, freq, word):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        else:
            return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    uses min head -> O(nlogk)
    """
    @staticmethod
    def run(words, k):
        counter = Counter(words)
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, Word(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)
        result = [""] * k
        for i in range(k):
            result[k-i-1] = heapq.heappop(heap).word
        return result


test_data = [[["i", "love", "leetcode", "i", "love", "coding"], 2], [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
