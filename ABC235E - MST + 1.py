def main():
    n, m, q = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        edges.append([c, a, b, -1]) # edges[3]: オリジナル辺:-1, 追加辺:i(0<=i<=Q-1)

    # クエリの追加辺を先読みしておく.
    # 追加辺を含めたM+Q個の辺で、Kruskal法でMSTを作ることを考える.
    # オリジナル辺の場合、通常通りMSTを作っていく.
    # a,bを結ぶ追加辺eiが選ばれたとき、既にオリジナル辺のMSTで結ばれているかを調べる.
    # Yes: MSTは追加辺eiを含まない, No: 追加辺eiを含む(ただしこの辺をMSTに追加してはいけない).

    additonal_edges = ['No']*q
    for i in range(q):
        u, v, w = map(int, stdin.readline().split())
        edges.append([w, u, v, i])

    edges = sorted(edges)

    uf = UnionFind(n)
    for i in range(m+q):
        _, ai, bi, ei = edges[i]
        # ei < 0: Gの辺の場合、普通にMSTを作っていく
        if ei<0:
            uf.union(ai-1, bi-1)

        # ei >= 0: 各クエリで追加する辺の場合、構成中のMSTでつながる前ならその辺がMSTに追加される
        else:
            # 既に2点を結ぶ辺がMSTにあるか?
            if uf.find(ai-1)==uf.find(bi-1):
                pass
            # ない場合、eiはGiのMSTに含まれる
            else:
                additonal_edges[ei] = 'Yes'

    print(*additonal_edges, sep='\n')


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

if __name__ == '__main__':
    from sys import stdin
    from math import sqrt, ceil, floor, factorial
    from collections import defaultdict, deque, Counter
    from heapq import heapify, heappop, heappush
    from itertools import accumulate, permutations, combinations, product
    import copy

    # int(input())
    # map(int, stdin.readline().split())
    # list(map(int, stdin.readline().split()))

    main()