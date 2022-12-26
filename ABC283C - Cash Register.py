def main():
  S = list(input().replace('\n', ''))
  N = len(S)
  ans = 0
  zeros = 0


  for i in range(N):
    s = S[i]

    if s=='0':
      zeros += 1

    else:
      tmp = math.ceil(zeros/2)
      ans += 1 + tmp
      zeros = 0

  tmp = math.ceil(zeros/2)
  ans += tmp


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