def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    uf = UnionFind(N)
    belonged = [collections.defaultdict(int) for _ in range(N)]
    for i in range(N):
        belonged[i][C[i]] += 1

    for _ in range(Q):
        t, a, b = map(int, sys.stdin.readline().split())

        if t==1:
            a -= 1
            b -= 1
            root_a = uf.find(a)
            root_b = uf.find(b)

            if root_a != root_b:
                uf.union(a, b)
                root_new = uf.find(a)
                if root_new==root_a:
                    for k, v in belonged[root_b].items():
                        belonged[root_new][k] += v
                    belonged[root_b].clear()
                else:
                    for k, v in belonged[root_a].items():
                        belonged[root_new][k] += v
                    belonged[root_a].clear()                    

        else:
            x, y = a-1, b
            root = uf.find(x)
            print(belonged[root][y])



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
    import sys
    import collections

    main()