def main():
    import sys
    N = int(input())
    E = []
    for _ in range(N-1):
        u, v, w = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        E.append((w, u, v))

    # 重みの小さい順に辺を追加して、森を木にしていく
    # 重みwの辺eがu, vを結ぶとき、この辺を追加する前はu, vは必ず非連結で、
    # u側の連結成分の重みはw以下、v側の連結成分の重みもw以下である
    # よって、u, vの連結成分の頂点数をそれぞれNu, Nvとすると、
    # Nu個の頂点 -> Nv個の頂点への単純パスでの最大の重みはwとなり、
    # このwは、Nu*Nv個のパスに寄与することとなる

    E.sort()
    uf = UnionFind(N)

    ans = 0
    for w, u, v in E:
        num_u = -uf.parents[uf.find(u)]
        num_v = -uf.parents[uf.find(v)]

        ans += w * (num_u*num_v)
        uf.union(u, v)

    print(ans)


####################################################################################################
####################################################################################################

class UnionFind():
    def __init__(self, n):
        self.n = n
        # root: -1 * num of elements, others: their own parent.
        # To show, write print(uf.parents).
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # path compression; search for root, and connect to each parent.
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # If not yet; return 1(Done), already; return 0(Nothing).
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # union by rank;
        #  connect less-depth group to higher-depth one not to increase max-depth.
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return 1

    def size(self, x):
        return -self.parents[self.find(x)]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == '__main__':

    main()