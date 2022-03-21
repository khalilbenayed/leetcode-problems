"""
https://leetcode.com/problems/word-search/
https://leetcode.com/problems/word-search-ii/

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

from copy import deepcopy
from test_runner import TestRunner

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def word_search(board, word):
        m, n = len(board), len(board[0])

        def explore(x, y):
            stack = [(x, y, {(x, y)})]
            while len(stack):
                curr_x, curr_y, seen = stack.pop()
                pos = len(seen)
                if pos == len(word):
                    return True
                for a, b in directions:
                    if 0 <= curr_x+a < m and 0 <= curr_y+b < n and \
                            board[curr_x+a][curr_y+b] == word[pos] and \
                            (curr_x+a, curr_y+b) not in seen:
                        stack.append((curr_x+a, curr_y+b, seen | {(curr_x+a, curr_y+b)}))
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and explore(i, j):
                    return True
        return False

    @staticmethod
    def old_word_search_ii(board, words):
        """Bad solution: search all words in the board... takes too long."""
        m, n = len(board), len(board[0])
        words = set(words)
        firsts = set([word[0] for word in words])

        def explore(seen, x, y):
            potential_words = {board[x][y]}
            for i, j in directions:
                if 0 <= x+i < m and 0 <= y+j < n and not seen[x+i][y+j]:
                    seen_copy = deepcopy(seen)
                    seen_copy[x+i][y+j] = True
                    potential_sub_words = explore(seen_copy, x+i, y+j)
                    potential_words |= set(map(lambda sub_word: board[x][y] + sub_word, potential_sub_words))
            return potential_words

        ans = set()
        for x in range(m):
            for y in range(n):
                if board[x][y] in firsts:
                    seen = [[False] * n for _ in range(m)]
                    seen[x][y] = True
                    potential_words = explore(seen, x, y)
                    ans |= words & potential_words
        return list(ans)

    @staticmethod
    def word_search_ii(board, words):
        """Better solution: search for specifics words in the board."""
        m, n = len(board), len(board[0])
        firsts = {word[0]: set() for word in words}
        for word in words:
            firsts[word[0]].add(word)

        def explore_recursive(x, y, word, seen):
            if len(word) <= 1:
                return True
            for i, j in directions:
                if 0 <= x+i < m and 0 <= y+j < n and board[x+i][y+j] == word[1] and not seen[x+i][y+j]:
                    seen_copy = deepcopy(seen)
                    seen_copy[x+i][y+j] = True
                    if explore_recursive(x+i, y+j, word[1:], seen_copy):
                        return True
            return False

        def explore_iterative(x, y, word):
            if len(word) <= 1:
                return True
            stack = [(x, y, [(x, y)])]
            while len(stack) != 0:
                a, b, path = stack.pop()
                if len(path) == len(word):
                    return True
                for i, j in directions:
                    if 0 <= a+i < m and 0 <= b+j < n and board[a+i][b+j] == word[len(path)] and (a+i, b+j) not in path:
                        stack.append((a+i, b+j, path + [(a+i, b+j)]))
            return False

        ans = []
        for x in range(m):
            for y in range(n):
                if board[x][y] in firsts:
                    for word in firsts[board[x][y]]:
                        # seen = [[False] * n for _ in range(m)]
                        # seen[x][y] = True
                        # found = explore_recursive(x, y, word, seen)
                        # found = explore_iterative(x, y, word)
                        if found:
                            ans.append(word)
                    firsts[board[x][y]] -= set(ans)
        return ans


# test_data = [
#     [[['A', 'B', 'C', 'E'],
#       ['S', 'F', 'C', 'S'],
#       ['A', 'D', 'E', 'E']], "ABCCED"],
#     [[['A', 'B', 'C', 'E'],
#       ['S', 'F', 'C', 'S'],
#       ['A', 'D', 'E', 'E']], "SEE"],
#     [[['A', 'B', 'C', 'E'],
#       ['S', 'F', 'C', 'S'],
#       ['A', 'D', 'E', 'E']], "ABCB"],
#     [[["A", "B", "C", "E"],
#       ["S", "F", "E", "S"],
#       ["A", "D", "E", "E"]], "ABCESEEEFS"],
# ]
# solutions = [Solution1.word_search]
# TestRunner.run(solutions, test_data)

test_data = [
    [[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]],
    [[["a","b"],["c","d"]], ["abcb"]],
    [[["a","a"]], ["aaa"]],
    [[["a","b","c"],
      ["a","e","d"],
      ["a","f","g"]], ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]]
]
solutions = [Solution1.word_search_ii]
TestRunner.run(solutions, test_data)
