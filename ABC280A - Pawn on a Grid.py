def main():
  H, W = map(int, input().split())
  ans = 0
  for i in range(H):
    x = list(input())
    for j in range(W):
      ans += 1 if x[j]=='#' else 0

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