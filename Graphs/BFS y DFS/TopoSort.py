def topoSort(G):
    n = len(G)
    indeg = [0 for i in range(n)]
    for u in range(n):
        for v in G[u]:
            indeg[v] += 1
    topo = []
    indeg0 = [i for i in range(n) if indeg[i] == 0]
    while len(topo) < n:
        i = indeg0.pop()
        topo.append(i)
        for j in G[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                indeg0.append(j)
    return topo

G = [[2, 4], [2], [], [0, 2], []]

print(topoSort(G))
