"""
https://leetcode.com/problems/minimum-area-rectangle-ii/

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

    1) group pairs of points by distance
    2) for every distance, check if any 2 pairs of points form a rectangle
    """
    @staticmethod
    def run(points):

        def dist(p1, p2):
            return ((p1[0] - p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5

        def intersect_in_middle(p1, p2, p3, p4):
            m1 = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
            m2 = ((p3[0]+p4[0])/2, (p3[1]+p4[1])/2)
            return m1 == m2

        distances = {}
        for i, p1 in enumerate(points):
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p1 != p2:
                    distance = dist(p1, p2)
                    if distance in distances:
                        distances[distance].append((p1, p2))
                    else:
                        distances[distance] = [(p1, p2)]

        min_area = None

        for distance, pairs in distances.items():
            for p1, p2 in pairs:
                for p3, p4 in pairs:
                    if dist(p1, p3) == dist(p2, p4) and dist(p1, p3) != 0 and dist(p1, p4) != 0 and dist(p2, p3) != 0 \
                     and intersect_in_middle(p1, p2, p3, p4):
                        print(1, p1, p2, p3, p4, dist(p1, p3) * dist(p1, p4))
                        area = dist(p1, p3) * dist(p1, p4)
                        min_area = min(min_area, area) if min_area else area
                    elif dist(p1, p4) == dist(p2, p3) and dist(p1, p3) != 0 and dist(p1, p4) != 0 and dist(p2, p4) != 0 \
                     and intersect_in_middle(p1, p2, p3, p4):
                        print(2, p1, p2, p3, p4, dist(p1, p3) * dist(p1, p4))
                        area = dist(p1, p3) * dist(p1, p4)
                        min_area = min(min_area, area) if min_area else area
        return min_area if min_area else 0


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    group by center and distance
    """
    @staticmethod
    def run(points):

        def dist(p1, p2):
            return ((p1[0] - p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5

        group_by = {}
        for i, p1 in enumerate(points):
            for j in range(i+1, len(points)):
                p2 = points[j]

                distance = dist(p1, p2)
                center = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
                key = (distance, center)
                if key in group_by:
                    group_by[key].append((p1, p2))
                else:
                    group_by[key] = [(p1, p2)]

        min_area = None
        for _, pairs in group_by.items():
            for i, (p1, p2) in enumerate(pairs):
                for j in range(i+1, len(pairs)):
                    p3, p4 = pairs[j]
                    area = dist(p1, p3) * dist(p1, p4)
                    if area != 0:
                        min_area = min(min_area, area) if min_area else area
        return min_area if min_area else 0


test_data = [[[[1,2],[2,1],[1,0],[0,1]]], [[[0,1],[2,1],[1,1],[1,0],[2,0]]], [[[0,3],[1,2],[3,1],[1,3],[2,1]]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
