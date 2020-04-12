"""G = [
    [3,7],
    [0],
    [1],
    [3],
    [],
    [4,6],
    [5],
    [1,5,8],
    [0,6],
    [1],
]"""

G = [[1, 6], [0, 2, 3, 5], [1, 3, 4], [1, 2, 4], [2, 3], [1, 6, 7, 8], [0, 5], [5, 8], [5, 7, 9], [8], [11], [10]]

#G = [[1], [2, 4], [2, 5], [1, 6], [0, 3], [7], [4], [8], [5]]

def dfs(u):
    global G, scc
    assert low[u]==depth[u]
    stack.append(u)
    in_stack[u] = 1
    for v in G[u]:
        if depth[v]==-1: # tree-edge
            depth[v] = low[v] = depth[u]+1
            dfs(v)
            low[u] = min(low[u], low[v])
        elif in_stack[v]: # back-edge
            low[u] = min(low[u], depth[v])

    if low[u] == depth[u]:
        aux = []
        while stack[-1]!=u:
            aux.append(stack.pop())
        aux.append(stack.pop())
        for x in aux:
            in_stack[x] = 0
        #print(aux)
        scc.append(aux)



def tarjan():
    global depth, low, stack, in_stack, scc, G
    n = len(G)
    depth = [-1 for i in range(n)]
    low = [-1 for i in range(n)]
    stack = []
    in_stack = [0 for i in range(n)]
    scc = []

    for i in range(n):
        if depth[i]==-1:
            depth[i] = low[i] = 0
            dfs(i)

    print("En el grafo hay {0} SCC".format(len(scc)))
    print("Los cuales son:")
    for i in range(len(scc)):
        print(scc[i])

tarjan()
