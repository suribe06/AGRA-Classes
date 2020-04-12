G = [
    [1],
    [0],
    [3],
    [4, 2],
    [3]
]

def list2matrix(G):
    n = len(G)
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in G[i]:
            M[i][j] = 1
    return M

for l in list2matrix(G):
    print(l)

def matrix2list(M):
    n = len(M)
    L = [[] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            if M[i][j] == 1:
                L[i].append(j)
    return L

r = matrix2list(list2matrix(G))
print(r)

def list2edgelist(G):
    n = len(G)
    E = []
    for i in range(n):
        for j in G[i]:
            E.append((i, j))
    return E, n

def edgelist2List(E, n):
    L = [[] for i in range(n)]
    for i,j in E:
        L[i].append(j)
    return L
