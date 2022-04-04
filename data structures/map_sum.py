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


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sum = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, new_val, old_val=0):
        curr = self.root
        for char in key:
            curr.sum += new_val - old_val
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.sum += new_val - old_val

    def search(self, key):
        curr = self.root
        for char in key:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.sum


class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.map:
            self.trie.insert(key, val, self.map[key])
            self.map[key] = val
        else:
            self.trie.insert(key, val)
            self.map[key] = val

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)


obj = MapSum()
obj.insert("aa", 3)
print(obj.sum("a"))
obj.insert("aa", 2)
print(obj.sum("a"))
print(obj.sum("aa"))
