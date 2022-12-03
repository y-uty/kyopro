
def main():
    import sys
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
       a, b, c = map(int, sys.stdin.readline().split())
       edges.append([c, a, b])

    edges.sort()

    # 連結のままでなるだけ辺を取り除くには、最小全域木を考えればよい.
    # Kruskal法.
    # union結果が「既に連結」の場合、その辺は最小全域木には不要で取り除ける.
    # ただし辺のコストが負の場合は取り除くと報酬が減るので残したままにする.
    uf = UnionFind(n)
    costs = 0
    for e in edges:
        c, p, q = e
        res = uf.union(p-1, q-1)
        if res==0 and c>0:
            costs += c
            
    print(costs)


class UnionFind(): # https://note.nkmk.me/python-union-find/
    def __init__(self, n):
        self.n = n
        # root: -1 * num of elements, others: their own parent
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x # その木の頂点数も返すように改修
        else:
            # path compression; search for root, and connect to each parent
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # Unionでグループ数(=連結成分)が減少したかを確認するために、0 or 1をreturnするように改修
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

    def size(self, x):
        return -self.parents[self.find(x)]

if __name__ == '__main__':
    main()