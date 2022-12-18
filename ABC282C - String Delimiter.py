def main():
  N = int(input())
  S = list(input().replace('\n', ''))

  quote_flag = 0
  ans = []
  for i in range(N):
    s = S[i]

    if s=='"':
      quote_flag ^= 1
    
    if s==',' and (not quote_flag):
      ans.append('.')
    else:
      ans.append(s)

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