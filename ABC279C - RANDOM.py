def main():
  # 1. S, Tの行ごとの#の数が一致であることがまず必要
  # 2. 次に、S, Tの列ごとの#の数を昇順にしたときにS, Tで一致することが必要
  H, W = map(int, input().split())

  Srowsum = []
  Scolsum = [0]*W
  for i in range(H):
    s = list(input().replace('\n', ''))
    tmp = 0
    for j in range(W):
      if s[j]=='#':
        tmp += 1
        Scolsum[j] += 1
    Srowsum.append(tmp)
  
  Trowsum = []
  Tcolsum = [0]*W
  for i in range(H):
    t = list(input().replace('\n', ''))
    tmp = 0
    for j in range(W):
      if t[j]=='#':
        tmp += 1
        Tcolsum[j] += 1
    Trowsum.append(tmp)
  

  # 1.の判定
  for i in range(H):
    if Srowsum[i]!=Trowsum[i]:
      print("No")
      exit()
  
  # 2.の判定
  Scolsum.sort()
  Tcolsum.sort()
  for j in range(W):
    if Scolsum[j]!=Tcolsum[j]:
      print("No")
      exit()


  print("Yes")



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