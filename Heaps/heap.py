"""def push(h, x):
    h.append(x)
    return

def top(h):
    return min(h)

def pop(h):
    x = min(h)
    i = h.index(x)
    h[:] = h[:i] + h[i+1:]
    return x"""

########################

def push(h, x):
    h.append(x)
    i = len(h) - 1
    while i != 1 and h[i] < h[i//2]:
        swap(h, i, i//2)
        i = i//2
    return

def top(h):
    return h[1]

def pop(h):
    swap(h, 1, len(h)-1)
    x = h.pop()
    i = 1
    m = -1
    while m != i:
        j, k = 2*i, 2*i+1
        m = i
        if j < len(h) and h[j] < h[m]: m = j
        if k < len(h) and h[k] < h[m]: m = k
        if m != i:
            swap(h, i, m)
            i = m
            m = -1
    return x

def swap(h, i, j):
    h[i], h[j] = h[j], h[i]
    return

h = [None]
push(h, 2)
print(top(h))
print(pop(h))
push(h, 1)
push(h, 3)
push(h, 0)
print(pop(h))
push(h, 2)
print(pop(h))
