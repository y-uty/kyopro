def main():
  N, M = map(int, input().split())
  G = collections.defaultdict(list)

  for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
  
  colored = [-1]*(N+1) # 二部グラフの塗り分け
  conn_no = [-1]*(N+1) # 頂点ごとの連結成分の番号
  visited = [False]*(N+1)
  num_col0_by_conn = [0]*(N+1) # 連結成分番号ごとの、色0の頂点の個数
  num_col1_by_conn = [0]*(N+1) # 連結成分番号ごとの、色1の頂点の個数

  no = 1
  for v_start in range(1, N+1):
    if not visited[v_start]:

      nx = collections.deque()
      nx.append(v_start)
      visited[v_start] = True
      colored[v_start] = 0 # 始点は必ず0で塗る
      num_col0_by_conn[no] += 1
      conn_no[v_start] = no
      while nx:
        v_from = nx.popleft()

        for v_to in G[v_from]:
          # toが塗られていない場合、fromと異なるほうの色で塗る
          if colored[v_to] < 0:
            colored[v_to] = colored[v_from] ^ 1
            if colored[v_to]==1:
              num_col1_by_conn[no] += 1
            else:
              num_col0_by_conn[no] += 1
          # toにすでに塗られた色が、fromと同じ場合、二部グラフではない
          elif colored[v_to]==colored[v_from]:
              print(0)
              exit()
          
          if not visited[v_to]:
            visited[v_to] = True
            conn_no[v_to] = no
            nx.append(v_to)

      no += 1 # 連結成分番号の加算

  ans = 0
  # 二部グラフとなった時点で、iと、すべてのG[i]の組は(0, 1), (1, 0)になっている
  # 各頂点について、相手を探す
  # 自分の連結成分には、異なる色で、自分と辺で直接つながっていない頂点があてはまる
  # それ以外の連結成分では、(連結成分が二部グラフになってさえいれば、)どの頂点と新たに辺を結んでも、二部グラフとなる
  for i in range(1, N+1):
    if colored[i]==0:
      ans += num_col1_by_conn[conn_no[i]] - len(G[i])
      ans += N - (num_col1_by_conn[conn_no[i]] + num_col0_by_conn[conn_no[i]])
    else:
      ans += num_col0_by_conn[conn_no[i]] - len(G[i])
      ans += N - (num_col1_by_conn[conn_no[i]] + num_col0_by_conn[conn_no[i]])


  print(ans//2)


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