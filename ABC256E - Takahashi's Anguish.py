def main():
    import heapq
    n = int(input())
    x = list(map(int, input().split()))
    c = list(map(int, input().split()))
    edges = []

    for i in range(n):
        heapq.heappush(edges, (-c[i], x[i]-1, i)) # 0-indexed
    uf = UnionFind(n)
    ans = 0

    while edges:
        cost, u, v = heapq.heappop(edges)

        ret = uf.union(u, v)
        if ret==0:
            ans -= cost

    print(ans)


# https://note.nkmk.me/python-union-find/

class UnionFind():
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