def main():
  N = int(input())
  # 色ごとに回収を終えて左端/右端にいるときの最小値を求めていく
  # dp[i][j]:= 色iを回収し終えて、色iがある座標のjの端(0:左, 1:右)に到達する最小コスト
  Colors = collections.defaultdict(list)
  for _ in range(N):
    X, C = map(int ,input().split())
    Colors[C].append(X)
  
  for k in Colors.keys():
    Colors[k].sort()
  
  CX = []
  for k, v in Colors.items():
    CX.append((k, v))
  CX.append((N+1, [0]))
  CX.sort() # 色番号の若い順

  ColNum = len(CX) # 色の種類数

  INF = 10**15
  dp = [[INF]*2 for _ in range(ColNum+1)]
  dp[0][0] = 0
  dp[0][1] = 0 # 開始地点(原点)は両端ともにx=0

  prevl, prevr = 0, 0 # 前の左端、右端
  for i in range(ColNum):
    _, Xs = CX[i]
    Xl, Xr = Xs[0], Xs[-1] # 次の左端、右端
    
    for j in range(2):
      prevX = prevl if j==0 else prevr
      if prevX <= Xl:
        dp[i+1][0] = min(dp[i+1][0], dp[i][j]+abs(Xr-prevX)+abs(Xr-Xl))
        dp[i+1][1] = min(dp[i+1][1], dp[i][j]+abs(Xr-prevX))
      elif Xl < prevX and prevX < Xr:
        dp[i+1][0] = min(dp[i+1][0], dp[i][j]+abs(Xr-prevX)+abs(Xr-Xl))
        dp[i+1][1] = min(dp[i+1][1], dp[i][j]+abs(prevX-Xl)+abs(Xr-Xl))
      else:
        dp[i+1][0] = min(dp[i+1][0], dp[i][j]+abs(Xl-prevX))
        dp[i+1][1] = min(dp[i+1][1], dp[i][j]+abs(prevX-Xl)+abs(Xr-Xl))
    
    prevl, prevr = Xl, Xr

  print(min(dp[-1]))


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
