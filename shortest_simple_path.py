
infty = 2**31


def find_shortest_simple_path(g, s, t):
    # a is the set of configurations
    a = [[s]]
    # d is table of shortest paths
    d = [infty for _ in g]
    d[s-1] = 0

    while len(a) != 0:
        c = a.pop()
        u = c[-1]

        val = 0
        for i in range(1, len(c)):
            val += g[c[i-1]-1][c[i]]

        if u == t and val < d[t-1]:
            d[t-1] = val
        elif val <= d[u-1]:
            d[u-1] = val
            for v in g[u-1]:
                if v not in c:
                    a.append(c+[v])
    return d[t-1] if d[t-1] < infty else 'No path'


g = [  # s:1, a:2, b:3, d:4, t:5, v:6
    {2: 1, 3: 2},
    {5: 1, 6: 1},
    {6: 1},
    {2: 1},
    {},
    {4: -1000},
]
print(find_shortest_simple_path(g, 1, 5))
