def main():
  N, K = map(int, input().split())
  A = list(map(int, input().split()))

  # dp[i]:= 石i個から先手が最適に行動したときの勝(1) or 負(0)
  dp = [0]*(K+1)

  for i in range(K):
    for a in A:
        if i+a <= K:
            # 一つでも勝になる選び方があるなら勝、一つもない時に限り負
            dp[i+a] |= dp[i]^1

  if dp[K]:
    print("First")
  else:
    print("Second")


if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
  from heapq import heappush, heappop, heapify
  import itertools
  import bisect
  import math
  import operator
  from functools import lru_cache

  main()