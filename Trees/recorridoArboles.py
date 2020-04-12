def preOrder(G, u, ans):
    ans.append(u)
    for v in G[u]:
        preOrder(G, v, ans)

def inOrder(G, u, ans):
    if len(G[u]) > 0:
        inOrder(G, G[u][0], ans)
    ans.append(u)
    for i in range(1, len(G[u])):
        inOrder(G, G[u][i], ans)

def posOrder(G, u, ans):
    for v in G[u]:
        posOrder(G, v, ans)
    ans.append(u)

G = [[1, 2], [3, 4], [], [], []]

ans1 = []
preOrder(G, 0, ans1)
print(ans1)

ans2 = []
inOrder(G, 0, ans2)
print(ans2)

ans3 = []
posOrder(G, 0, ans3)
print(ans3)
