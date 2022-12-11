def main():
  N, Ma, Mb = map(int, input().split())
  P = [ tuple(map(int, input().split())) for _ in range(N) ]

  # dp[i][j][k]:= i個目まで見てAがjグラム、Bがkグラムとなるような最小コスト
  INF = 10**9
  dp = [[[INF]*(N*10+1) for _ in range(N*10+1)] for _ in range(N+1)]
  dp[0][0][0] = 0

  for i in range(N):
    a, b, c = P[i]
    for j in range(N*10+1):
      for k in range(N*10+1):

        if dp[i][j][k] < INF:

          # 買う
          dp[i+1][j+a][k+b] = min(dp[i+1][j+a][k+b], dp[i][j][k]+c)

          # 買わない
          dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])


  # Ma, Mbは互いに素なので、Ma:Mbが成り立つように、(Ma, Mb), (2Ma, 2Mb), ...を見ていく
  ans = INF
  A, B = Ma, Mb
  while A <= N*10 and B <= N*10:
    ans = min(ans, dp[N][A][B])
    A += Ma
    B += Mb
  
  if ans < INF:
    print(ans)
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