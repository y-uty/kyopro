def main():
  N = int(input())
  p = list(map(float, input().split()))

  # dp[i][j]:= コインiまで投げて、表がj回出る確率
  dp = [[0]*(N+1) for _ in range(N+1)]
  dp[0][0] = 1

  for i in range(N):
    pi = p[i]
    for j in range(i+1):
      # 表が出る
      dp[i+1][j+1] += dp[i][j] * pi
      # 裏が出る
      dp[i+1][j] += dp[i][j] * (1-pi)
  
  print(sum(dp[N][(N+1)//2:]))



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