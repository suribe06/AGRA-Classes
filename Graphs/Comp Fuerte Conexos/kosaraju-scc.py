def dfs(u,num):
	global vis, scc, G
	vis[u] = 1
	scc[u] = num
	for v in G[u]:
		if(vis[v] == 0):
			dfs(v,num)

def dfs_list(u):
	global L, vis, I
	vis[u] = 1
	for v in I[u]:
		if(vis[v] == 0):
			dfs_list(v)
	L.append(u)


def compute(G):
	global L,I, scc, vis
	n = len(G)
	scc = [-1 for i in range(n)]

	I = [[] for i in range(n)]
	for i in range(n):
		for j in G[i]:
			I[j].append(i)
	vis = [0 for i in range(n)]
	L = []
	for i in range(n):
		if(vis[i] == 0):
			dfs_list(i)
	vis = [0 for i in range(n)]
	cont = 0
	while(len(L)):
		i = L.pop()
		if(vis[i] == 0):
			dfs(i,cont)
			cont +=	1
	return scc

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
	[1]
]"""

G = [[3, 7, 8, 12, 13], [4], [1, 7, 8, 11, 12, 13, 14], [10], [4, 6, 8], [5, 6, 8, 12, 14], [], [7, 14], [7, 10, 14], [2, 11], [], [1, 6, 8], [2, 6, 8, 13], [1, 4, 5, 7], [2, 3]]

scc = compute(G)
print(scc)
for i,x in enumerate(scc):
	print(i,x)

