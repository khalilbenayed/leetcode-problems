import heapq

### Q1 ###

def combineParts(parts):
    """
    Strategy:
    At every step, pick the pairs with the smallest combined size, combine them and continue until there is only one part left.

    Proof of correctness:
    This algorithm uses a greedy approach to solve the problem. So we can use induction to prove correctness. Let n be the number of parts.
    * Base case: For n=2, clearly the two parts have the two smallest sizes (trivially) so this works.
    * Induction step: assume for k>2 parts the algorithm above gives the minimum time to combine k parts. Let's prove it works for k+1 parts.
        We can use the algorithm for the k parts with least size, we are left with 2 parts which we can combine.
        This is therefore the most optimal way to combine all the parts

    Runtime:
    Let n be the number of parts. At every step, we combine two parts to produce a part, so the number of parts decreases by 1.
    Hence we will have O(n) steps. Now in every step, we find the two smallest parts, which can be done in O(n) time, hence the total runtime
    would be O(n^2). But we can use a min heap to store the parts which decreases the runtime. The runtime to build the heap is O(n log n), and
    at every step finding the two smallest parts and pushing the resulting part take O(log n) each. In conclusion, the combined runtime is O(n log n).
    """

    heapq.heapify(parts)
    time = 0
    while len(parts) > 1:
        item1, item2 = heapq.heappop(parts), heapq.heappop(parts)
        time += item1 + item2
        heapq.heappush(parts, item1+item2)
    return time


### Q2 ###

def distanceTraversed(grid):
    """
    Strategy:
    Find where the obstacle is in the grid, then use A* search to find the minimum distance to it. Use the manhattan distance as a heuristic.
    The manhattan distance is an admissible heuristic, hence the solution found by this algorithm is optimal.

    The runtime of this algorithm is exponential, as we might have to try all possible paths before finding the obstacle.
    The space complexity is O(n*m), as we might have to store all nodes in the frontier.
    """
    m, n = len(grid), len(grid[0])

    # first make sure the robot does not start in a trench
    if grid[0][0] == 0:
        return -1

    # first find the obstacle
    target = (0, 0)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 9:
                target = (i, j)
                break

    # now perform A* search
    def manhattanDistance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    pos = (0,0)
    priority = manhattanDistance(pos, target)
    distance = 0
    frontier = [(priority, pos, distance)]
    seen = {pos}

    while len(frontier) != 0:
        cost, pos, distance = heapq.heappop(frontier)
        if pos == target:
            return distance
        x, y = pos
        seen.add(pos)
        for i, j in directions:
            if 0 <= x+i < m and 0 <= y+j < n and grid[x+i][y+j] != 0 and (x+i, y+j) not in seen:
                new_pos = (x+i, y+j)
                priority = cost + manhattanDistance(new_pos, target)
                heapq.heappush(frontier, (priority, new_pos, distance+1))

    # if reached here no possible solution
    return -1


ex1 = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,0,0],
    [1,1,0,0,9]
]
print(distanceTraversed(ex1))