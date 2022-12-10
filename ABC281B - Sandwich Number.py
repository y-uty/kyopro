def main():
  S = list(input().replace('\n', ''))
  lenS = len(S)

  if lenS != 8:
    print("No")
    exit()
  
  AtoZ = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  if S[0] not in AtoZ:
    print("No")
    exit()
  
  if S[-1] not in AtoZ:
    print("No")
    exit()

  num = list('0123456789')

  for i in range(1, 7):
    s = S[i]
    if s not in num:
      print("No")
      exit()
    
    if i==1 and s=='0':
      print("No")
      exit()


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