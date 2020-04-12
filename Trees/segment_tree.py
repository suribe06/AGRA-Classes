A = [10, 6, 7, -5]

class SegmentTree:
    def __init__(self, A):
        n_hojas = 1
        while n_hojas < len(A):
            n_hojas *= 2

        self.tree = [0 for i in range(2 * n_hojas)]
        self.tree[0] = 'BASURA'
        for i in range(len(A)):
            self.tree[i + n_hojas] = A[i]

        for i in range(n_hojas - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

        self.n_hojas = n_hojas
        return

    def suma(self, lo, hi, i=1):
        if lo == hi:
            ans = 0
        else:
            ans = self._suma(lo, hi, i=1, L=0, R=self.n_hojas)
        return ans

    def _suma(self, lo, hi, i, L, R):
        assert L <= lo < hi <= R
        M = (L + R) // 2
        if L == lo and R == hi:
            ans = self.tree[i]
        elif hi <= M: #Recurro sobre hijo izquierdo
            ans = self._suma(lo, hi, 2*i, L, M)
        elif lo >= M: #Recurro sobre hijo derecho
            ans = self._suma(lo, hi, 2*i+1, M, R)
        else:
            ans = self._suma(lo, M, 2*i, L, M)
            ans += self._suma(M, hi, 2*i+1, M, R)

        return ans

    def set(self, i, val):
        i = i + self.n_hojas
        self.tree[i] = val
        while i != 1:
            pa = i // 2
            self.tree[pa] = self.tree[2*pa] + self.tree[2*pa+1]
            i = pa
        return

    def printTree(self):
        print(self.tree)
        return

print(A)
S = SegmentTree(A)
S.printTree()
print(S.suma(1, 1))
