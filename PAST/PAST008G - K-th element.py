def main():
  N, K = map(int, input().split())
  P = [ tuple(map(int, input().split())) for _ in range(N) ]
  
  # K番目の数をDとすると、各数列のD以下の数の総和はちょうどK個になる
  # (各数列のどこかにD自身が含まれることに注意)
  # D未満の数では、必ずその総和はK未満となり、
  # また、D以上の数では、必ずその総和はK以上となり、これは単調性を持つ
  # よって、D以下の総和がK個以上になるような数Dの最小値が答え
  # (K個以下になる最大値、だと成り立つDに上限がなくなる場合があるので最小値で考える)

  def is_ok(x):
      Y = 0 # 各数列にx以下の項がいくつあるかの総和
      for i in range(N):
        A, B, C = P[i]
        if x < B:
          continue
        else:
          Y += min((x-B)//C + 1, A)
      
      if Y >= K:
        return True
      else:
        return False


  # 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
  ok, ng  = 10**18, 0
  def bin_srch_mgr(ok, ng):
      while abs(ok-ng) > 1:
          mid = (ok+ng) // 2
          if is_ok(mid): ok = mid
          else: ng = mid
      return ok

  ans = bin_srch_mgr(ok, ng)
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
  import copy

  main()