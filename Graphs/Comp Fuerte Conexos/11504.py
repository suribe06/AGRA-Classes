from sys import stdin


def solve(G):
    return

def main():
    global G
    cases = int(stdin.readline())
    while cases > 0:
        n, m = stdin.readline().strip().split()
        G = [[] for _ in range(int(n))]
        for edge in range(int(m)):
            i, j = stdin.readline().strip().split()
            G[int(i) - 1].append(int(j) - 1)
        solve(G)
        G = []
        cases -= 1

main()
