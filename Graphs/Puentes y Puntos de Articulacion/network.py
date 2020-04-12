visited, parent = None, None

def dfs(G):
    global visited, parent
    visited = [0 for _ in G]
    parent = [-1 for _ in G]
    for u in range(len(G)):
        if visited[u] == 0:
            dfs_visit(G, u)

def dfs_visit(G, u):
    visited[u] = 1
    for v in G[u]:
        if visited[v] == 0:
            parent[v] = u
            dfs_visit(G, v)
    visited[u] = 2

def solve(graph):
    dfs(graph)
    print(visited)
    print(parent)
    

graph = [[4], [4], [4], [4], [0, 1, 2, 3]]

print(solve(graph))
