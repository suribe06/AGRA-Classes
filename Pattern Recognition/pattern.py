def text_search(T, P):
    M, N = len(T), len(P)
    ans = False
    if M >= N:
        low = 0
        while ans == False and low + N <= M:
            hi = 0
            while hi != N and P[hi] == T[low + hi]:
                hi += 1
            ans, low = hi == N, low + 1

    return ans

a = "abracadabra"
b = "cada"

print(text_search(a, b))
