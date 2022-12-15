def main():
  N = int(input())
  A = [0] + list(map(int, input().split()))
  MOD = 998244353

  # 1/xの逆元を前計算; 1/xをかけることはxの逆元をかけることと同じ
  INV = [0]
  for i in range(1, N+1):
    INV.append(pow(i, MOD-2, MOD))
  
  # dp[i]:= マスiから始めたとき、ゴールするのに必要な回数の期待値; 答えはdp[1]
  # dp[N] = 0 (すでにゴールしている)
  # dp[i] = 1/(A[i]+1) * (dp[i]+dp[i+1]+dp[i+2]+...+dp[i+A[i]]) + 1
  # dp[i]を左辺に移行して整理すると
  # dp[i] = {1/(A[i]+1) * Σ(k=1~A[i])(dp[i+K]) + 1} * (A[i]+1)/A[i]
  # シグマの部分は、累積和を取っていくかBinary Indexed Treeを使うなどする(後者で間に合いそう)
  dp = [0]*(N+1) 
  dp[N] = 0
  FT = BIT(N) # Binary Indexed Tree

  for i in range(N-1, 0, -1): # N-1 -> 1
    p = INV[A[i]+1]
    csum = FT.get(i+A[i]) - FT.get(i)
    E = (p * csum + 1) * (A[i]+1) * INV[A[i]]
    E %= MOD
    dp[i] = E
    FT.add(i, E)
  
  print(dp[1])


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