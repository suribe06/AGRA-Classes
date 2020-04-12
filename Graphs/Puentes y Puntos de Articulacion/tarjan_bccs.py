def tarjan():
    global G, depth, low
    n = len(G)
    depth = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]
    for u in range(n):
        if depth[u] == -1:
            depth[u] = low[u] = 0
            dfs(u)
    print(depth)
    print(low)
    return

def dfs(u):
    global G, depth, low
    for v in G[u]:
        if depth[v] == -1: #u, v es tree edge
            depth[v] = low[v] = depth[u] + 1
            dfs(v)
            low[u] = min(low[u], low[v])
        elif depth[u] - depth[v] == 1: # u, v es parent edge
            pass
        elif depth[v] < depth[u] - 1: # u, v es back edge
            low[u] = min(low[u], depth[v])

        elif depth[v] > depth[u]: # u, v es down edge
            pass
    return

G = [[4], [4], [4], [4], [0, 1, 2, 3]]


tarjan()




