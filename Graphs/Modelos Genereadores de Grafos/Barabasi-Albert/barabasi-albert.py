"""Model generation for Barabasi-Albert graphs (BA-graphs) to build an
approximation for the degree distribution. It plots such an
approximation.

"""

from random import *
from sys import *
import matplotlib.pyplot as plt

seed     = int(argv[1])         # random seed
rand     = Random(seed)
N        = int(argv[2])         # total number of nodes
M        = int(argv[3])         # number of connections from/to incomming vertices
test_cnt = int(argv[4])         # number of runs to collect averages

assert N>=0 and M>=0 and test_cnt>0

def build_graph(n, m):
  """Builds a graph with n vertices using the Barabasi-Albert model
  where each new arriving node connects to m of the exisiting ones
  using preferential attachment on the vertex degree measure
  """
  assert n>=0 and m>=0
  graph,rept = list(),list()
  while len(graph)!=n:
    u,mm = len(graph),min(len(graph), m)
    newed = set()
    while len(newed)!=mm: newed.add(rand.choice(rept))
    graph.append(list(newed))
    rept.extend( [ u for _ in range(len(newed)+1) ] )
    for x in graph[u]:  # graph[u] == graph[-1]
      rept.append(x)
      graph[x].append(u)
  return graph

def degree_freq(graph):
  """collects the degree frequency in the given graph"""
  ans = [ 0 for _ in range(len(graph)) ]
  for ul in graph: ans[len(ul)] += 1
  return ans

def rstripzeroes(a):
  """removes all zeroes at the end of a list of integers"""
  while len(a)!=0 and a[-1]==0: a.pop()

def main():
  """performs int(argv[4]) experiments, generating an BA(int(argv[2]),
int(argv[3])) per run, to approximate the expected degree distribution
for such graphs
  """
  accum = [ 0 for _ in range(N) ]
  for _ in range(test_cnt):
    deg = degree_freq(build_graph(N, M))
    for i in range(N): accum[i] += deg[i]
  rstripzeroes(accum)
  accum = [ accum[i]/test_cnt for i in range(len(accum)) ]
  print(accum)
  plt.stem(accum)
  plt.title('Degree distribution')
  plt.xlabel('degree')
  plt.ylabel('# nodes with a given degree')
  plt.show()
    
main()
