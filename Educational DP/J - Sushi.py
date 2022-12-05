def main():
  N = int(input())
  A = list(map(int, input().split()))
  a = collections.Counter(A)
  a1, a2, a3 = a[1], a[2], a[3]

  # dp[i][j][k]:= 1個の皿i枚、2個の皿j枚、3個の皿k枚 から全て食べ切るまでの回数の期待値
  # 0個の皿、1個の皿、2個の皿、3個の皿を選ぶ確率をそれぞれp0, p1, p2, p3とすると、
  # dp[i][j][k] = dp[i-1][j][k]*p1 + dp[i+1][j-1][k]*p2 + dp[i][j+1][k-1]*p3 + dp[i][j][k]*p0 + 1
  
  # このままだと両辺にdp[i][j][k]がいて求められないので、移項して消去する
  # dp[i][j][k]*(1-p0) = dp[i-1][j][k]*p1 + dp[i+1][j-1][k]*p2 + dp[i][j+1][k-1]*p3 + 1
  # dp[i][j][k] = {dp[i-1][j][k]*p1 + dp[i+1][j-1][k]*p2 + dp[i][j+1][k-1]*p3 + 1} / (1-p0)

  dp = [[[0.0]*(a3+2) for _ in range(a3+a2+2)] for _ in range(a3+a2+a1+2)]
  for k in range(a3+1): # 3個の皿は初期の枚数から増えることはない
    for j in range(a3+a2+1-k): # 2個の皿は初期の(3個の皿+2個の皿)の枚数から増えることはない
      for i in range(a3+a2+a1+1-k-j): # 1個の皿は、最大でN枚まで増える
        if i==0 and j==0 and k==0: continue
        E1 = dp[i-1][j][k] if i-1 >= 0 else 0
        E2 = dp[i+1][j-1][k] if j-1 >= 0 else 0
        E3 = dp[i][j+1][k-1] if k-1 >= 0 else 0
        dp[i][j][k] = (E1*(i/N) + E2*(j/N) + E3*(k/N) + 1) * (N/(i+j+k))
  
  print(dp[a1][a2][a3])



if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
  from heapq import heappush, heappop, heapify
  import itertools
  import bisect
  import math
  import operator
  from functools import lru_cache

  main()