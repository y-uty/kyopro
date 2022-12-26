def main():
  ## Phase 1
  N = int(input())

  # create sparse table
  M = 0
  K = N.bit_length()
  tab = []
  for i in range(K): # 2^i
    l = 1 << i
    row = []
    for j in range(N-l+1):
      M += 1
      row.append((j+1, j+l, M))
    tab.append(row)

  print(M)
  sys.stdout.flush()
  for i in range(K):
    for j in tab[i]:
      print(*j[:2])
      sys.stdout.flush()

  ## Phase 2
  Q = int(input())

  for _ in range(Q):
    L, R = map(int, input().split())
    X = R-L+1
    Y = X.bit_length()-1
    interval1 = tab[Y][L-1]
    interval2 = tab[Y][R-2**Y]
    print(interval1[2], interval2[2])
    sys.stdout.flush()



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