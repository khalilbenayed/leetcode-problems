"""
https://leetcode.com/problems/minimum-height-trees/

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

    brute force: compute height for every node as root
    """
    @staticmethod
    def run(n, edges):
        graph = {}
        for u, v in edges:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]

        def dfs(root):
            stack = [(root, 1)]
            visited = set()
            max_height = 1
            while len(stack) != 0:
                curr, height = stack.pop()
                visited.add(curr)
                max_height = max(max_height, height)
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        stack.append((neighbour, height + 1))
            return max_height
        dic = {}
        for node in range(n):
            height = dfs(node)
            if height in dic:
                dic[height].append(node)
            else:
                dic[height] = [node]
        return dic[min(dic.keys())]


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(n, edges):
        # first find longest path in this tree
        graph = {}
        for u, v in edges:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
            if v in graph:
                graph[v].append(u)
            else:
                graph[v] = [u]

        def bfs(root):
            queue = [(root, 1)]
            visited = set()
            distance, endpoint = 0, None
            parents = {root: None}
            while len(queue) != 0:
                curr, height = queue.pop(0)
                visited.add(curr)
                if height > distance:
                    distance = height
                    endpoint = curr
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        queue.append((neighbour, height + 1))
                        parents[neighbour] = curr
            path = []
            while endpoint is not None:
                path.append(endpoint)
                endpoint = parents[endpoint]
            return path
        s = bfs(0)[0]
        path = bfs(s)

        if len(path) % 2 == 1:
            return [path[len(path) // 2]]
        return path[len(path)//2-1:len(path)//2+1]


test_data = [[4, [[1,0],[1,2],[1,3]]],[6, [[3,0],[3,1],[3,2],[3,4],[5,4]]]]
solutions = [Solution1.run, Solution2.run]
TestRunner.run(solutions, test_data)
