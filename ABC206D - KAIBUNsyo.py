def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 数の書き換えを、数を頂点/書き換えを辺 として無向グラフで考える.
    # 同じ数が別ペアでも登場するなら、それらも一緒に書き換わるから、
    # Union-Findでつなげていって、連結成分ごとに書き換えの回数を調べればよい.
    # 結局、最後には1つの数字に書き換わるので、その回数は連結成分の頂点数-1.
    # これは最後にUnion-Find.parents配列のrootに持っている頂点数を使えばよい.

    uf = UnionFind(max(a))

    for i in range(n//2):
        if a[i]!=a[-1-i]:
            uf.union(a[i]-1, a[-i-1]-1)
    
    ans = 0
    for p in uf.parents:
        if p < 0: # 根には、その連結成分の頂点数が格納されている.
            ans -= p+1
    
    print(ans)

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