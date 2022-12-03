import sys
import collections
n, m = map(int, input().split())


class UnionFind():
    def __init__(self, n):
        self.n = n
        # root: -1 * num of elements, others: their own parent
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # path compression; search for root, and connect to each parent
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]


    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # union by rank;
        #  connect less-depth group to higher-depth one not to increase max-depth
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return 1

l = collections.defaultdict(list)
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    l[a].append(b)
    l[b].append(a)

    ret = uf.union(a-1, b-1)
    if ret==0:
        print('No')
        exit()

for v in l.values():
    if len(v) >= 3:
        print('No')
        exit()

print('Yes')