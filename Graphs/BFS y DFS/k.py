def failure(A):
    M = len(A)
    fail = [None for _ in range(M)]
    j = 0
    for i in range(1, M):
        fail[i] = j
        while j > 0 and A[i] != A[j]:
            j = fail[j]
        j += 1
    return fail

def kmp(T, P):
    T = " " + T
    P = " " + P
    N = len(T)
    M = len(P)
    j = 1
    fail = failure(P)
    for i in range(1, N):
        while j > 0 and T[i] != P[j]:
            j = fail[j]
        if j == M - 1:
            return i - M + 1
        j += 1
    return None
