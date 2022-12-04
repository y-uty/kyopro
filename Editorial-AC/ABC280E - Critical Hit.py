def main():
  N, P = map(int, input().split())
  MOD = 998244353

  # dp[i]:= 体力iから0以下にする攻撃回数の期待値
  # dp[0] = 0 (もう攻撃不要)
  # dp[1] = 1 (1回攻撃すれば必ず体力0以下にできる)
  # k >= 2 について、クリティカル率をpとすると、
  # dp[k] = (dp[k-2] + 1) * p + (dp[k-1] + 1) * (1 - p)
  # p = P/100 より、100の逆元Rを求めておけば、p = PR となる

  R = pow(100, MOD-2, MOD)
  dp = [0]*(N+1)
  dp[1] = 1
  for i in range(2, N+1):
    dp[i] = (dp[i-2]+1) * P*R + (dp[i-1]+1) * (1-P*R)
    dp[i] %= MOD
  
  print(dp[N])

  

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