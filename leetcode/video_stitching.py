"""
https://leetcode.com/problems/video-stitching/

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

    Greedy
    """
    @staticmethod
    def run(clips, t):
        clips = sorted(clips)

        ans = 0
        i, reach = 0, 0
        while i < len(clips) and clips[i][0] <= reach < t:
            max_reach = reach
            while i < len(clips) and clips[i][0] <= reach:
                if clips[i][1] > max_reach:
                    max_reach = clips[i][1]
                i += 1
            ans += 1
            reach = max_reach

        if reach < t:
            return -1
        return ans


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    DP
    """
    @staticmethod
    def run(clips, t):
        m = [0] * max(max(clips, key=lambda clip: clip[1])[1], t)
        for clip in clips:
            m[clip[0]] = max(m[clip[0]], clip[1])

        for i in range(1, t):
            m[i] = max(m[i], m[i-1])

        if m[0] == 0:
            return -1

        ans, reach, i = 0, 0, 0
        while reach < t:
            reach = m[i]
            if reach <= i:
                return -1
            i = reach
            ans += 1

        return ans




test_data = [[[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10], [[[0,1],[1,2]], 5], [[[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
