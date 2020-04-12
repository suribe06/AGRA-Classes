
from sys import stdin
from heapq import heappush, heappop

global INF

INF = float('inf')

def solve():
    global source, target, G, ans, dist, visited
    visited = [False for _ in range(len(G))]
    dist = [INF for i in range(len(G))]
    dist[source] = 0
    queue = [(0, source)]

    while len(queue) != 0:
        d, u = heappop(queue)
        if visited[u] == False:
            visited[u] = True
            for v, w in G[u]:
                duv = d + w
                if visited[v] == False and dist[v] > duv:
                    dist[v] = duv
                    heappush(queue, (duv, v))

def main():
    global source, target, G, dist, visited
    cases = int(stdin.readline())
    for c in range(cases):
        lenv, lene, source, target = map(int, stdin.readline().split())
        G = [list() for _ in range(lenv)]
        for _ in range(lene):
            u, v, w = map(int, stdin.readline().split())
            if u != v:
                G[u].append((v, w))
                G[v].append((u, w))

        solve()
        if(visited[target] != -1 and dist[target] != INF):
            print('Case #{0}: {1}'.format(c+1, dist[target]))
        else:
            print('Case #{0}: unreachable'.format(c+1))

main()
