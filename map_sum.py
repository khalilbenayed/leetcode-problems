"""
https://leetcode.com/problems/map-sum-pairs

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
from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.children = defaultdict()
        self.val = 0


class Trie:

    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, word, val):
        root = self.root
        old_val = self.map.get(word, 0)

        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
            root.val += val - old_val

        self.map[word] = val

    def search_prefix(self, prefix):
        root = self.root
        for char in prefix:
            root = root.children[char]

        return root.val


class MapSum:
    def __init__(self):
        """Initialize your data structure here."""
        self.trie = Trie()

    def insert(self, key, val):
        self.trie.insert(key, val)

    def sum(self, prefix):
        sum = self.trie.search_prefix(prefix)
        return sum


obj = MapSum()
obj.insert("aa", 3)
print(obj.sum("a"))
obj.insert("aa", 2)
print(obj.sum("a"))
print(obj.sum("aa"))
