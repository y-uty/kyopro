def main():
  N = int(input())
  A = list(map(int, input().split()))
  MOD = 998244353

  # A[L]<=A[R] であるような左端L, 右端Rを選ぶと、
  # 条件を満たす連続とは限らない部分列は、L < i < R の部分は何を選んでも良いから、
  # 2^(R-L-1) 個存在する
  # これを(L, R)の組について全探索すると、O(N^2)だが、これを高速化したい

  # Rを固定して、それより左のindexについてだけ、A[L]<=A[R]を満たすLを考える
  # 2^(R-L-1) = 2^(R-1) / 2^L より、A[L]<=A[R]を満たすLについて、
  # 各Rについて Σ(L) 2^(R-1) / 2^L = 2^(R-1) * Σ(L) {1/(2^L)} を求めればよい
  # これは、A[i]の値をindexとして、左から登場順に1/(2^i)を加算していく配列を用意するとして、
  # A[L]<=A[R]を満たすLにおける総和を、Binay Idexed Treeなどの区間和データ構造をその配列とすることで
  # 高速に求めることが可能である (Σの中身は、各Rにおいて[0, A[R]]の区間和を求めれば良い)
  # ただし、以下に注意
  #  1. A[i]<=10^9なので、予め座標圧縮が必要
  #  2. 1/(2^i)の総和を小数で扱いながら求めるのは難しいため、逆元で求めておく
  #     つまり、1/(2^i)≡R (mod p)について(2^i)の逆元Qを求めると 1*Q≡R (mod p) で、このRを加算する

  # 座標圧縮
  A = compression(A)

  # 2^iとその逆元の前計算
  EXP2 = []
  INV = []
  x = 1
  for _ in range(N):
    EXP2.append(x)
    INV.append(pow(x, MOD-2, MOD))
    x *= 2
    x %= MOD

  # BITで答えを求めつつ登場した値に対する1点加算を行う
  ans = 0
  FT = BIT(N)
  FT.add(A[0], INV[0])

  for R in range(1, N):
    # 2^(R-1) * Σ(L) {1/(2^L)} を求める
    ans += EXP2[R-1] * FT.get(A[R])
    ans %= MOD

    # 今回登場したものの1点更新
    FT.add(A[R], INV[R])
  

  print(ans)



# 二分探索による配列の座標圧縮(1-indexed)
def compression(a, x_indexed=1):
    a_unique = sorted(list(set(a)))
    acomp = []
    for i in range(len(a)):
        ng, ok  = -1, len(a_unique)
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if a_unique[mid] >= a[i]: ok = mid
            else: ng = mid
        acomp.append(ok+x_indexed)
    return acomp

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

  main()