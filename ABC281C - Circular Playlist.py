def main():
  N, T = map(int, input().split())
  A = list(map(int, input().split()))
  B = [A[0]]
  for i in range(1, N): B.append(B[-1]+A[i])

  tot = sum(A)
  t = T%tot

  stt = 0
  for i, b in enumerate(B):
    if t < b:
      print(i+1, abs(t-stt))
      exit()
    
    stt = b


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