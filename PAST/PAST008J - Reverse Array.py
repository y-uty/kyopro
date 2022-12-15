def main():
  N, Q = map(int, input().split())

  # まず、どのように反転操作を繰り返しても、
  # 位置は(1, 2N), (2, 2N-1), ..., (N, N+1)のペアで入れ替わるだけである
  # よって、それぞれ何回反転したかさえわかれば、その偶奇によってペアのどちらが答えかを場合分けすればよい

  # t=1のクエリでkが与えられたとき、l<=kを満たすようなすべての「中心からl番目」が反転するから、
  # 反転区間の左端をBinary Indexed Treeでもって加算していくことで、
  # O(log k)で「k以上N以下の区間の反転回数の総和」を求めることができる
  # あとは、k > Nのときに扱う添字に注意して適切に場合分けすれば良い

  FT = BIT(N)
  
  for _ in range(Q):
    t, k = map(int, input().split())

    if t==1:
      
      if k <= N: # 左半分
        cnt = FT.get(N) - FT.get(N-k)
        if cnt%2:
          print(2*N-k+1)
        else:
          print(k)

      else: # 右半分
        m = 2*N-k+1
        cnt = FT.get(N) - FT.get(N-m)
        if cnt%2:
          print(m)
        else:
          print(k)

    else:  
      if k <= N:
        FT.add(k, 1)
      else:
        FT.add(2*N-k+1, 1)


class BIT():
    def __init__(self, n, id_elem=0):
        self.id_elem = id_elem
        self.bit = [id_elem]*n
        self.bit_size = n+1

    def add(self, i, x):
        # i: bitの要素番号(1-indexed)
        # x: bit[i]に対して作用させる値
        while i < self.bit_size:
            self.bit[i-1] += x
            i += i & -i # 最後の1のビットを加算

    def get(self, i):
        # i: 1~iまでの累積作用結果を取得する(1-indexed)
        ret = self.id_elem # 単位元で初期化
        while i > 0:
            ret += self.bit[i-1]
            i -= i & -i # 最後の1のビットを減算
        return ret



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