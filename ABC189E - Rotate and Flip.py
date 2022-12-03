def main():
  N = int(input())
  koma = [ tuple(map(int, input().split())) for _ in range(N) ]
  E = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
  A = [E] # Ai := i回操作後の累積作用の行列

  def dot(X, Y, n):
    a = [0]*(n*n)
    for k in range(n*n):
      for i in range(n):
          a[k] += X[k//n][i]*Y[i][k%n]
    
    return [a[n*i:n*(i+1)] for i in range(n)]

  M = int(input())
  for _ in range(M): 
    op = list(map(int, input().split()))
    t = op[0]
  
    if t==1: # 原点まわり-90度回転
      A.append(dot([[0, 1, 0], [-1, 0, 0], [0, 0, 1]], A[-1], 3))

    elif t==2: # 原点まわり90度回転
      A.append(dot([[0, -1, 0], [1, 0, 0], [0, 0, 1]], A[-1], 3))

    elif t==3: # x=pについて反転 x' = p+(p-x) = 2p-x
      p = op[1]
      A.append(dot([[-1, 0, 2*p], [0, 1, 0], [0, 0, 1]], A[-1], 3))

    else: # y=pについて反転 y' = 2p-y
      p = op[1]
      A.append(dot([[1, 0, 0], [0, -1, 2*p], [0, 0, 1]], A[-1], 3))


  Q = int(input())
  for _ in range(Q):
    a, b = map(int, input().split())
    b -= 1

    A_a = A[a]
    koma_b = [koma[b][0], koma[b][1], 1]

    ans_x, ans_y = 0, 0
    for i in range(3):
      ans_x += A_a[0][i]*koma_b[i]
      ans_y += A_a[1][i]*koma_b[i]

    print(ans_x, ans_y)


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