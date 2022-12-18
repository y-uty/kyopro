def main():
  N, M = map(int, input().split())
  ans = 0

  S = []
  for i in range(N):
    x = list(input())
    s = []
    for j in range(M):
      if x[j]=='o':
        s.append(1)
      else:
        s.append(0)
    S.append(s)
  
  for i in range(N-1):
    for j in range(i+1, N):
      ok = 0
      for k in range(M):
        if S[i][k] | S[j][k]:
          ok += 1
      
      if ok==M:
        ans += 1

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