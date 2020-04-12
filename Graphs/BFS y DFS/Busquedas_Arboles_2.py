G = [[3, 4], [5], [5], [0, 4], [0, 3], [1, 2, 6], [5]]

def dfs(u):
    global G, vis
    vis[u] = 1
    for v in G[u]:
        if vis[v] == 0:
            dfs(v)
    return

def count_CCs():
  global G, vis
  n = len(G)
  cnt = 0
  vis = [0 for i in range(n)]
  for u in range(n):
      if vis[u] == 0:
          dfs(u)
          cnt += 1
  return cnt

print(count_CCs())
