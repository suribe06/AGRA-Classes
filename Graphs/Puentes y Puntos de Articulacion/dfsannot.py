from sys import stdin

graph,lenv = None,None

visited,parent = None,None
tin,tout,time = None,None,None

def dfs(G):
  '''recursive DFS algorithm for a graph G in adjacency list
     representation with vertices V = { 0, 1, len(G)-1 }
  '''
  global visited,parent,time,tin,tout
  visited = [ 0 for _ in G ]
  parent = [ -1 for _ in G ]
  tin = [ None for _ in G ]
  tout = [ None for _ in G ]
  time = 0
  for u in range(len(G)):
    if visited[u]==0:
      dfs_visit(G, u)

def dfs_visit(G, u):
  global visited,tin,tout,time
  visited[u],tin[u],time = 1,time,time+1
  for v in G[u]:
    if visited[v]==0:
      parent[v] = u
      dfs_visit(G, v)
  visited[u],tout[u],time = 2,time,time+1

def solve():
  dfs(graph)
  print(visited)
  print(parent)
  print(tin)
  print(tout)
  
def main():
  global graph,lenv
  lenv = int(stdin.readline())
  while lenv!=0:
    graph = [ set() for _ in range(lenv) ]
    tok = [ int(x) for x in stdin.readline().split() ]
    while tok[0]!=0:
      for i in range(1, len(tok)):
        graph[tok[0]-1].add(tok[i]-1)
        graph[tok[i]-1].add(tok[0]-1)
      tok = [ int(x) for x in stdin.readline().split() ]
    print(solve())
    lenv = int(stdin.readline())

main()
