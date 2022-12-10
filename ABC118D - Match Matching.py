def main():
  N, M  = map(int, input().split())
  A = list(map(int, input().split()))
  req = [0,2,5,5,4,5,6,3,7,6]

  # dp[i][j]:= マッチをi本目まで使って、j個めに作れる最大の数字
  K = N//2
  dp = [[-1]*(K+1) for _ in range(N+1)]
  dp[0][0] = 0
  for i in range(N):
    for j in range(min(i+1, K+1)):

      if dp[i][j] >= 0:
        for a in A:
          use = req[a]
          if i+use <= N:
            if a > dp[i+use][j+1]:
              dp[i+use][j+1] = a
  
  # 復元
  for j in range(K, -1, -1):
    if dp[N][j] > 0:
      C = j
      break
  
  ans = []
  R = N
  while C > 0:
    num = dp[R][C]
    ans.append(str(num))
    C -= 1
    R -= req[num]
  
  ans.sort(reverse=True)
  print(''.join(ans))
    


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