from collections import deque

G = [
    [1],
    [0],
    [3],
    [4, 2],
    [3]
]

def bfs(src, G, vis):
    q = deque()
    q.append(src)
    vis[src] = 1
    while len(q):
        u = q.popleft()
        for v in G[u]:
            if vis[v] == 0:
                vis[v] = 1
                q.append(v)
    return

def dfs(u, G, vis):
    vis[u] = 1
    for v in G[u]:
        if vis[v] == 0:
            dfs(v, G, vis)
    return

def dfs_iterative(G, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for i in G[vertex]:
            stack.append(i)

    return path


def countCC_BFS(G):
    """Cuenta la cantidad de CCS en G utilizando BFS"""
    n = len(G)
    vis = [0 for i in range(n)]
    cnt = 0
    for i in range(n):
        if vis[i] == 0:
            bfs(i, G, vis)
            cnt += 1
    return cnt

print(dfs(0, G, []))
