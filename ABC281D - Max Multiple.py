def main():
  N, K, D = map(int, input().split())
  A = list(map(int, input().split()))

  # dp[i][j][k]:= Aiまでからkこ選んだ総和がl*D+jとなるときのlの最大値
  dp = [[[-1]*(K+1) for _ in range(D)] for _ in range(N+1)]
  dp[0][0][0] = 0

  for i in range(N):
    for j in range(D):
      for k in range(K+1):

        if dp[i][j][k] >= 0:

          # Aiを使う
          if k < K:
            tmp_sum = dp[i][j][k]*D + j
            d_t, m_t = tmp_sum//D, tmp_sum%D
            next_sum = tmp_sum + A[i]
            d_n, m_n = next_sum//D, next_sum%D

            dp[i+1][m_n][k+1] = max(dp[i+1][m_n][k+1], d_n)
          
          # Aiを使わない
          dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

  if dp[N][0][K] >= 0:
    print(dp[N][0][K]*D)
  else:
    print(-1)



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