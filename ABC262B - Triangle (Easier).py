def main():
    n, m = map(int, input().split())
    G = defaultdict(set)

    for _ in range(m):
        u, v = map(int, stdin.readline().split())
        G[u-1].add(v-1)
        G[v-1].add(u-1)

    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                a = G[i]
                if j in a:
                    b = G[j]
                    if k in b:
                        c = G[k]
                        if i in c:
                            ans += 1

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