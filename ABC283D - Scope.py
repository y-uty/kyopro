def main():
  S = list(input().replace('\n', ''))
  N = len(S)

  box = collections.defaultdict(int)

  lv = 1
  for i in range(N):
    s = S[i]

    if s=='(':
      lv += 1

    elif s==')':
      for k in box.keys():
        if box[k] == lv:
          box[k] = 0
      
      lv -= 1

    else:
      if box[s] > 0:
        print("No")
        exit()

      else:
        box[s] = lv


  print("Yes")





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