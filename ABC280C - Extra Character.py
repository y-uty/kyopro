def main():
  S = list(input().replace('\n', '')) + ['_']
  T = list(input().replace('\n', ''))

  for i, s in enumerate(S):
    t = T[i]
    if s!=t:
      print(i+1)
      exit()


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