def main():
  N, M = map(int, input().split())
  A = list(map(int, input().split()))

  # ペアの作り方だけ考えると、N頂点に対してN(N-1)/2通りある
  # ペアを作ることは、その中から辺を選んで頂点を結んでいくことに等しい
  # 今回は、ペアを一度に選び、「片方はもう一度選べる」「他方はもう選べない」となることから、
  # 1回のペア作成ごとに、1頂点が候補から消えていく -> N人が1vs1で試合をするごとに1人脱落するイメージ
  # すると、ペア作成、つまり辺を選ぶ回数はN-1回である
  # つまり、N頂点N-1辺で、かつ全ての頂点が必ず1度は選ばれる(誰かと結ぶ辺を持つ)=連結であることから、
  # 木を作ることを考えれば良い

  # N(N-1)/2辺について、(x^y + y^x)%M の結果をそのまま重みとしてもてば、
  # 木を作るために必要な辺の集合を、それらの重みの和が最大になるように選べば良く、これはMSTである

  E = []
  # (x^y + y^x)%M の重みをもつ辺をN(N-1)本つくる
  for i in range(N-1):
    for j in range(i+1, N):
      x, y = A[i], A[j]
      s = pow(x, y, M) + pow(y, x, M)
      s %= M
      E.append((s, i, j))
  
  # MST, ただし最大にしたいので重みの降順にsort
  E.sort(reverse=True, key=operator.itemgetter(0))
  # クラスカル法
  uf = UnionFind(N)
  ans = 0
  for s, i, j in E:
    if uf.same(i, j):
      continue
    ans += s
    uf.union(i, j)
  
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