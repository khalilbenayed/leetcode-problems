"""
https://leetcode.com/problems/number-of-paths-with-max-score/

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
import heapq
from test_runner import TestRunner

class Solution1(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    DFS - time limit exceeded
    """
    @staticmethod
    def run(board):
        m, n = len(board), len(board[0])
        stack = [(m-1, n-1, 0)]
        max_score, count = 0, 0
        while len(stack) != 0:
            x, y, score = stack.pop()
            if (x, y) == (0, 0):
                if score > max_score:
                    max_score = score
                    count = 1
                elif score == max_score:
                    count += 1
                continue
            if x-1 >= 0 and y-1 >= 0 and board[x-1][y] == 'X' and board[x][y-1] == 'X' and board[x-1][y-1] != 'X' and score + 9 * (x + y - 2) >= max_score:
                stack.append((x-1, y-1, score + (int(board[x-1][y-1]) if board[x-1][y-1] != 'E' else 0)))
            else:
                if x-1 >= 0 and board[x-1][y] != 'X' and score + 9 * (x + y - 1) >= max_score:
                    stack.append((x-1, y, score + (int(board[x-1][y]) if board[x-1][y] != 'E' else 0)))
                if y-1 >= 0 and board[x][y-1] != 'X' and score + 9 * (x + y - 1) >= max_score:
                    stack.append((x, y-1, score + (int(board[x][y-1]) if board[x][y-1] != 'E' else 0)))

        return max_score, count


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    A* Search - time limit exceeded
    """
    @staticmethod
    def run(board):
        m, n = len(board), len(board[0])
        heap = [(0, m-1, n-1)]
        min_score, count = 0, 0
        while len(heap) != 0:
            score, x, y = heapq.heappop(heap)
            if (x, y) == (0, 0):
                if score < min_score:
                    min_score = score
                    count = 1
                elif score == min_score:
                    count += 1
                continue
            if x-1 >= 0 and y-1 >= 0 and board[x-1][y] == 'X' and board[x][y-1] == 'X' and board[x-1][y-1] != 'X' and score - 9 * (x + y - 1) <= min_score:
                heapq.heappush(heap, (score - (int(board[x-1][y-1]) if board[x-1][y-1] != 'E' else 0), x-1, y-1))
            else:
                if x-1 >= 0 and board[x-1][y] != 'X' and score - 9 * (x + y - 1) <= min_score:
                    heapq.heappush(heap, (score - (int(board[x-1][y]) if board[x-1][y] != 'E' else 0), x-1, y))
                if y-1 >= 0 and board[x][y-1] != 'X' and score - 9 * (x + y - 1) <= min_score:
                    heapq.heappush(heap, (score - (int(board[x][y-1]) if board[x][y-1] != 'E' else 0), x, y-1))

        return -min_score, count


class Solution3(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    DP: dp[i][j] = max_score, count for path from start to (i, j)
    """
    @staticmethod
    def run(board):
        m, n = len(board), len(board[0])
        dp = [[(0, 0)] * n for _ in range(m)]
        i, j = 1, 1
        dp[0][0] = (0, 1)
        while i < m and board[i][0] != 'X':
            dp[i][0] = (dp[i-1][0][0] + int(board[i][0]), 1)
            i += 1
        while j < n and board[0][j] != 'X':
            dp[0][j] = (dp[0][j-1][0] + int(board[0][j]), 1)
            j += 1

        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == 'X':
                    continue
                if board[i-1][j] == 'X' and board[i][j-1] == 'X' and board[i-1][j-1] != 'X':
                    dp[i][j] = dp[i-1][j-1][0] + (int(board[i][j]) if board[i][j] != 'S' else 0), dp[i-1][j-1][1]
                else:
                    max_score, count = 0, 0
                    if board[i-1][j] != 'X':
                        max_score, count = dp[i-1][j][0], dp[i-1][j][1]

                    if board[i][j-1] != 'X' and dp[i][j-1][0] == max_score:
                        count += dp[i][j-1][1]
                    elif board[i][j-1] != 'X' and dp[i][j-1][0] > max_score:
                        max_score, count = dp[i][j-1][0], dp[i][j-1][1]

                    if max_score == 0:  # no path possible here
                        continue

                    dp[i][j] = max_score + (int(board[i][j]) if board[i][j] != 'S' else 0), count
        return dp[m-1][n-1]


test_data = [[["E23","2X2","12S"]], [["E12","1X1","21S"]], [["E11","XXX","11S"]], [["EX","XS"]], [["E11345","X452XX","3X43X4","44X312","23452X","1342XS"]
]]
solutions = [Solution1.run, Solution2.run, Solution3.run]
TestRunner.run(solutions, test_data)


"""
"E11345"
"X452XX"
"3X43X4"
"44X312"
"23452X"
"1342XS"

[(0, 1), (1, 1), (2, 1), (5, 1), (9, 1), (14, 1)],
[(0, 0), (5, 1), (10, 1), (12, 1), (0, 0), (0, 0)],
[(0, 0), (0, 0), (14, 1), (17, 1), (0, 0), (0, 0)],
[(0, 0), (0, 0), (0, 0), (20, 1), (21, 1), (23, 1)],
[(0, 0), (0, 0), (0, 0), (25, 1), (27, 1), (0, 0)],
[(0, 0), (0, 0), (0, 0), (27, 1), (0, 0), (29, 1)]
"""