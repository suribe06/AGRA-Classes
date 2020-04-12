import random
random.seed(23)

def BA(N, M):
    assert N >= 0
    G = []
    rep = []
    i = 0
    while len(G) != N:
        u, minM = len(G), min(len(G), M)
        temp = set()
        while len(temp) != minM:
            node = random.choice(rep)
            tmp.add(node)

        for l in range(len(G[i]) + 1):
            rep.append(i)
        i += 1

    return G

print(BA(3, 2))
