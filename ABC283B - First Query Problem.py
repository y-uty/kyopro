def main():
  N = int(input())
  A = [0] + list(map(int, input().split()))
  Q = int(input())

  for _ in range(Q):
    qry = list(map(int, input().split()))

    if qry[0]==1:
      _, k, x = qry
      A[k] = x
    
    else:
      _, k = qry
      print(A[k])


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