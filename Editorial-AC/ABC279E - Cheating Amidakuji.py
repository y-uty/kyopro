def main():
  N, M = map(int, input().split())
  A = list(map(int, input().split()))
  for i in range(M): A[i] -= 1 # indexとして使うので-1しておく

  # 0, 1, 2, ..., i-1回まで操作した後の1の位置X1を求め、
  # 逆からM, M-1, ..., i+1回まで操作した後のB[X1]を調べる
  X = [0] # X[i]:= i回操作した後の1の位置(0-indexed)
  perm = [0]*N
  perm[0] = 1
  B = list(range(1, N+1))

  # 1の位置を正順に調べる
  for i in range(M):
    L = A[i]
    R = L+1

    if perm[L]==1:
      X.append(R)
    elif perm[R]==1:
      X.append(L)
    else:
      X.append(X[-1])
    perm[L], perm[R] = perm[R], perm[L]


  # Bの並びを逆順に調べながら答えを求める
  ans = []
  for i in range(M-1, -1, -1):
    ans.append(B[X[i]])

    L = A[i]
    R = L+1
    B[L], B[R] = B[R], B[L]
  
  print(*ans[::-1])




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