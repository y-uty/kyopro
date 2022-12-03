def main():
  N = int(input())
  S = list(map(int, input().split()))
  ans = []
  tmpsum = 0

  for i in range(N):
    s = S[i]
    ans.append(s-tmpsum)

    tmpsum = s
  
  print(*ans)




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