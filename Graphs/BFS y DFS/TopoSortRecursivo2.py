def dfs(u):
    global topo, visited
    visited[u] = True
    for v in G[u]:
        if visited[v] == False:
            dfs(v)
    topo.append(u)

def toposort(G):
    global topo, visited
    n = len(G)
    visited = [False for _ in range(n)]
    topo = []
    for i in range(n):
        if visited[i] == False:
            dfs(i)

    return topo

#G = [[2, 4], [2], [], [0, 2], []]
#G = [[], [], [3], [1], [0, 1], [0, 2]]
G = [[3], [0, 3], [], [], [0, 2]]

print(toposort(G))
