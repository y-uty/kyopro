def main():
  S = input().replace('\n', '')
  T = input().replace('\n', '')

  if T in S:
    print("Yes")
  else:
    print("No")


if __name__=="__main__":
  import sys
  input = sys.stdin.readline
  import collections
  import heapq
  import itertools
  import bisect
  import math
  import operator

  main()