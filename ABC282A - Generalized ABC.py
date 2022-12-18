def main():
  K = int(input())

  AtoZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  ans = []
  for i in range(K):
    ans.append(AtoZ[i])

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