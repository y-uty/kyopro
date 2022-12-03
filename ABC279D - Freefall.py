def main():
  A, B = map(int, input().split())
  
  if A < B:
    print(A)
    exit()

  def is_ok(g):
      fg = (A/(g**(0.5)) + B*(g-1))
      fg1 = (A/((g+1)**(0.5)) + B*g)

      if fg1 - fg >= 0:
        return True
      else:
        return False

  # 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
  def bin_srch_mgr(ok, ng):
      while abs(ok-ng) > 1:
          mid = (ok+ng) // 2
          if is_ok(mid): ok = mid
          else: ng = mid
      # print(ok)
      return ok

  ok = A//B
  ng = 0

  g_best = bin_srch_mgr(ok, ng)
  ans = A/(g_best**0.5) + B*(g_best-1)
  print(ans)


if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
  import heapq
  import itertools
  import bisect
  import math
  import operator
  main()