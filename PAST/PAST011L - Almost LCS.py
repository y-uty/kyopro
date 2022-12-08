def main():
  S = list(input().replace('\n', ''))
  T = list(input().replace('\n', ''))
  K = int(input())
  lenS, lenT = len(S), len(T)
  
  # dp[k][i][j]:= k文字書き換えたときのSのi文字目までとTのj文字目までの最長共通部分列の長さ
  dp = [[[0]*(lenT+1) for _ in range(lenS+1)] for _ in range(K+1)]
  for k in range(K+1):
    for i in range(1, lenS+1):
      for j in range(1, lenT+1):

        # Sのi文字目とTのj文字目が一致する
        if S[i-1]==T[j-1]:
           dp[k][i][j] = max(dp[k][i][j], dp[k][i-1][j-1]+1)
            
        # 一致しない
        else:
          # S[i]をT[j]に書き換える
          if k < K:
            dp[k+1][i][j] = max(dp[k+1][i][j], dp[k][i-1][j-1]+1)

          # 書き換えない
          dp[k][i][j] = max(dp[k][i][j], dp[k][i-1][j], dp[k][i][j-1])
    
  ans = 0
  for k in range(K+1):
    ans = max(ans, dp[k][lenS][lenT])
  
  print(ans)



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