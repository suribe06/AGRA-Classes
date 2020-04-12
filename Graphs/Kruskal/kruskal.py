class dforest(object):
  """Disjoint-Union implementation with disjoint forests using path
  compression and ranking"""

  def __init__(self, size=100):
    """create an empty disjoint forest"""
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 0 for _ in range(size) ]

  def __str__(self):
    """return the string representation"""
    return str(self.__parent)

  def find(self, x):
    """return the representative of x"""
    if self.__parent[x]!=x:
        self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self, x, y):
    """perform the union of the collections where x and y belong"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      krx,kry = self.__rank[rx],self.__rank[ry]
      if krx>=kry:
        self.__parent[ry] = rx
        if krx==kry: self.__rank[rx] += 1
      else:
        self.__parent[rx] = ry

def kruskal(G, lenv):
  ans = list()
  G.sort(key=lambda x: x[2])
  df = dforest(lenv)
  for u,v,w in G:
    if df.find(u)!=df.find(v):
      ans.append((u, v, w))
      df.union(u, v)
  return ans

G = [ (0, 1, 5),
      (0, 5, 4),
      (1, 2, 1),
      (1, 3, 8),
      (1, 7, 5),
      (2, 4, 4),
      (2, 5, 2),
      (2, 6, 1),
      (3, 4, 4),
      (5, 6, 3),
      (5, 7, 2),
      (6, 8, 6) ]

sol = kruskal(G, 9)
print(sol)
