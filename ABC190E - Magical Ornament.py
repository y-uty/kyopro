def main():
  N, M = map(int, input().split())
  G = collections.defaultdict(list)
  for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
  
  K = int(input())
  C = [0] + list(map(int, input().split()))

  # C1~CKそれぞれを始点とした最短距離をK回のBFSで求めてからTSP
  # TSPを意識して、0<->(任意の頂点)のコストを0としておく(0->0の巡回でTSPできる)
  INF = 10**9
  cost = [[INF]*(N+1) for _ in range(K+1)] # cost[i][j]:= C[i]を始点としたjまでの最短距離
  for i in range(K+1): cost[i][0] = 0
  for j in range(N+1): cost[0][j] = 0

  for i in range(1, K+1):
    v_start = C[i]
    nx = collections.deque()
    nx.append(v_start)
    visited = [False]*(N+1)
    visited[v_start]
    cost[i][v_start] = 0

    while nx:
      v_from = nx.popleft()
      for v_to in G[v_from]:
        if not visited[v_to]:
          cost[i][v_to] = cost[i][v_from] + 1
          visited[v_to] = True
          nx.append(v_to)

  # TSPの前に可否判定
  for j in range(K+1):
    if cost[1][C[j]]==INF:
      print(-1)
      exit()

  # bitDPによるTSPの計算量 O(N^2 2^N)
  # dp[i][j]:= 訪問済み頂点集合iで、現在位置がjのときの移動距離のMin
  dp = [[INF]*(K+1) for _ in range(2**(K+1))]
  dp[0][0] = 0

  for i in range(2**(K+1)): # 集合iが訪問済みで、
    # (終点である始点が訪問済み -> それ以上移動する必要がないのでSkip)
    if i%2: continue

    for j in range(K+1): # 現在地jの状態から、
      # (jが未訪問 -> iにjが含まれていないことになり、その経路はありえないのでSkip)
      if dp[i][j] < INF:

        for k in range(K+1): # 次の訪問先kへ移動する.
          # (kが訪問済み -> iに含まれる地点をもう一度訪れる必要がないのでSkip)
          if (i//(1<<k))%2 == 0:

          # 遷移
            dp[i | (1<<k)][k] = min(dp[i | (1<<k)][k], dp[i][j]+cost[j][C[k]])

  print(dp[2**(K+1)-1][0] + 1)



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