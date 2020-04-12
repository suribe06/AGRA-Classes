def dfs(i):
    vis[i] = 1
    for j in G[i]:
        if vis[j] == 0:
            dfs(j)
    topo.append(i)
    return

G = [[3], [0, 3], [], [], [0, 2]]
topo = []
n = len(G)
vis = [0] * n

for i in range(n):
    if vis[i] == 0:
        dfs(i)

print(topo)
