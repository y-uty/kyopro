import sys
import collections
n, m, k = map(int, input().split())

# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return 1

    def size(self, x):
        return -self.parents[self.find(x)]

fri = UnionFind(n)
fricnt = collections.defaultdict(int)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    fri.union(a-1, b-1)
    fricnt[a] += 1
    fricnt[b] += 1

blc = collections.defaultdict(list)
for _ in range(k):
    c, d = map(int, sys.stdin.readline().split())
    blc[c].append(d)
    blc[d].append(c)

ans = []
for i in range(1, n+1):
    grp_i = fri.find(i-1)
    blc_cnt = 0
    for x in blc[i]:
        grp_x = fri.find(x-1)
        if grp_i == grp_x:
            blc_cnt += 1

    ans.append(fri.size(i-1)-fricnt[i]-blc_cnt-1)

print(*ans)