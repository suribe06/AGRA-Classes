def f(T):
    if len(T) == 1:
        ans = 0
    else:
        ans = max(f(X) for X in T[1:])
        l = sorted([1 + X[0] for X in T[1:]])
        if len(l) == 1:
            ans = max(ans, l[0])
        else:
            ans = max(ans, l[-1] + l[-2])
    return ans

def add_G(T):
    if len(T) == 0:
        ans = [0]
    else:
        Y = [add_G(X) for X in T]
        ans = [1 + max(X[0] for X in Y)] + Y
    return ans
