def main():
  N, W, L, R = map(int, input().split())
  X = [0] + list(map(int, input().split())) + [W]
  MOD = 1000000007

  dp = [0]*(N+2)
  dp[0] = 1
  csum = [0]*(N+2)
  csum[0] = 1

  for i in range(N+1):
    # 起点にできる位置の左端と右端を二分探索で求める
    far = X[i+1]-R
    near = X[i+1]-L
    far_pos = bisect.bisect_left(X, far)
    near_pos = bisect.bisect_right(X, near)-1

    # 累積和を用いて、[左端, 右端]に含まれる通り数の総和を求める
    if near_pos==-1: # 起点の右端が0未満の場合、到達不可
      dp[i+1] = 0    
    elif far_pos==0:
      dp[i+1] = csum[near_pos]
    else:
      dp[i+1] = csum[near_pos] - csum[far_pos-1]
    dp[i+1] %= MOD
    
    # 累積和を計算
    csum[i+1] = csum[i] + dp[i+1]    
    csum[i+1] %= MOD


  print(dp[N+1])


if __name__=="__main__":
    import sys
    input = sys.stdin.readline
    import collections
    import heapq
    import itertools
    import bisect
    import math

    main()  