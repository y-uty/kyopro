def main():
  N, M = map(int, input().split())

  # M個の情報それぞれについて、mod 2で考えると、Ax,Ay=0or1, Ax+Ay≡1 or Ax+Ay≡0 となる
  # たとえば入力例2の1~3番目の情報では、A1+A2≡1, A2+A3≡0, A1+A3≡1
  # それぞれの式について、一方が0or1どちらか決めると、他方も決まる
  # たとえばA1=1とすると、A2=0, A3=0と芋づる式に決めていくことができる
  # 以上より、N頂点0辺のグラフに、M個の各X, Yについて頂点X, Yを結ぶ無向辺をはり、
  # 最終的なグラフの連結成分ごとに、少なくとも1つの頂点について0or1を確定させてやればよい
  # すなわち、答えは連結成分の個数
  uf = UnionFind(N)

  for _ in range(M):
    X, Y, _ = map(int, input().split())
    X -= 1
    Y -= 1
    uf.union(X, Y)
  
  ans = 0
  for p in uf.parents:
    if p < 0: ans += 1
  
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
    
    def same(self, x, y):
        return self.find(x) == self.find(y)


if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
  from heapq import heappush, heappop, heapify
  import itertools
  import bisect
  import math
  import operator
  import copy

  main()