"""
https://leetcode.com/problems/path-with-maximum-probability/

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
    """
    @staticmethod
    def run(n, edges, probs, s, t):
        # first build the graph
        graph = {u: {} for u in range(n)}
        for (u, v), prob in zip(edges, probs):
            graph[u][v] = prob
            graph[v][u] = prob

        # run modified dijkstra's algorithm
        seen, node_probs = [False] * n, [0] * n
        node_probs[s] = 1

        def max_prob():
            best_node, max_prob_so_far = -1, -1
            for i in range(n):
                if not seen[i] and node_probs[i] > max_prob_so_far:
                    best_node, max_prob_so_far = i, node_probs[i]
            return best_node, max_prob_so_far

        for _ in range(n):
            u, path_prob = max_prob()
            if u == t:
                return path_prob
            seen[u] = True
            for v, edge_prob in graph[u].items():
                node_probs[v] = max(node_probs[v], path_prob * edge_prob)
        return 0


class Solution2(object):
    """
    Details about it's time and space complexity. what makes it a good solution?
    """
    @staticmethod
    def run(n, edges, probs, s, t):
        # first build the graph
        graph = {u: {} for u in range(n)}
        for (u, v), prob in zip(edges, probs):
            graph[u][v] = prob
            graph[v][u] = prob

        # run modified dijkstra's algorithm
        heap = [(-1, s)] + [(0, u) for u in range(n) if u != s]
        nodes_in_heap = {u for u in range(n)}
        node_probs = [0] * n
        node_probs[s] = 1

        def modify_prob(u, prob):
            index = heap.index((-node_probs[u], u))
            heap[index] = (prob, u)
            heapq.heapify(heap)

        while len(heap) != 0:
            neg_path_prob, u = heapq.heappop(heap)
            path_prob = -neg_path_prob
            nodes_in_heap.remove(u)

            if u == t:
                return path_prob
            for v, edge_prob in graph[u].items():
                new_path_prob = path_prob * edge_prob
                if v in nodes_in_heap and node_probs[v] < new_path_prob:
                    modify_prob(v, -new_path_prob)
                    node_probs[v] = new_path_prob
        return 0


class Solution3(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    A* search
    """
    @staticmethod
    def run(n, edges, probs, s, t):
        # first build the graph
        graph = {u: {} for u in range(n)}
        for (u, v), prob in zip(edges, probs):
            graph[u][v] = prob
            graph[v][u] = prob

        # run A* search
        frontier = [(-1, s)]
        seen = set()

        while len(frontier) != 0:
            neg_path_prob, u = heapq.heappop(frontier)
            if u == t:
                return -neg_path_prob

            seen.add(u)
            for v, edge_prob in graph[u].items():
                if v not in seen:
                    heapq.heappush(frontier, (neg_path_prob * edge_prob, v))
        return 0


class Solution4(object):
    """
    Details about it's time and space complexity. what makes it a good solution?

    A* search
    """
    @staticmethod
    def run(n, edges, probs, s, t):
        # first build the graph
        graph = {u: {} for u in range(n)}
        for (u, v), prob in zip(edges, probs):
            graph[u][v] = prob
            graph[v][u] = prob

        # run DFS/BFS search
        frontier = [s]
        path_probs = {u: 0 for u in range(n)}
        path_probs[s] = 1

        while len(frontier) != 0:
            u = frontier.pop(0)
            path_prob = path_probs[u]
            if u == t:
                return path_prob

            for v, edge_prob in graph[u].items():
                if path_prob * edge_prob > path_probs[v]:
                    path_probs[v] = path_prob * edge_prob
                    frontier.append(v)
        return 0


test_data = [[3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2],
             [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2],
             [3, [[0,1]], [0.5], 0, 2],
             [5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]], [0.37,0.17,0.93,0.23,0.39,0.04], 3, 4]]
solutions = [Solution1.run, Solution2.run, Solution3.run, Solution4.run]
TestRunner.run(solutions, test_data)
