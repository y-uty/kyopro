def main():
  N, M = map(int, input().split())
  G = collections.defaultdict(list)
  T = [] # 片側未定のテレポータ

  for _ in range(M):
    U, V = map(int, input().split())
    if U==0:
      T.append(V)
    else:
      G[U].append(V)
      G[V].append(U)

  # テレポータの使い方によって答えのパターンがいくつかありそうなので、それらを予め求めてi=1~Nごとに最小値をとれないか考える
  # 以下、到達不能な場合の距離はINFとする

  # まず、片側未定テレポータを使わない場合、距離は1->Nの距離で、これはBFSでわかる

  # 次に、片側未定テレポータ(確定側T, 未定側tとする)を1回だけ使う場合を考える
  # この場合、1 -> T -> t -> N　という移動が考えられ、この距離は 1->T + 1 + t->N　である
  # よって、N->1のBFSもしておいて、t->Nの距離を求める
  # また、Nに近いほうが確定、1に近い方が未定もありうるので、同様に 1->t + 1 + T->N もある
  # ここで、tは未定側なので、解答時のi=1~Nを入れればよいが、Tはどの頂点だろうか？
  # 未定側の頂点が決まったとき、確定側はどのテレポータを使っても同じ頂点(=未定側)に移動することになる
  # よって、ありうるすべてのtについて、距離1->t, t->Nを、それぞれ1->N, N->1のBFSの結果から調べて、
  # その最小値となる(tの値によらない)

  # さらに、片側未定テレポータを2回使う場合を考える
  # 2回使う場合、1回目を使った後、2回目を使う前に他の頂点を移動するのはムダ(すぐに2回目のテレポータへ向かえばよいので)
  # よって、1から1回め使うまでの最短 + 1回め使った移動 + すぐに2回め使って移動 + 2回目使ったあとからNまでの最短
  # が最適となり、min(1->t) + 1 + 1 + min(t->N) で、前述の考察より、これはtの値によらずわかる

  # なお、3回以上使うことを考える必要はない
  # なぜならば、まず同じ頂点を2回通ることはないのでtを経由するのは1回だけでよいし、
  # 1->T1->t->T2->T3->N のような3回使用をするなら、T2を経由するのは明らかにムダだからである


  INF = 10**9
  dist1toN = bfs(G, 1, [INF]*(N+1)) 
  distNto1 = bfs(G, N, [INF]*(N+1)) 

  dist1toT = INF
  distNtoT = INF
  for t in T:
    dist1toT = min(dist1toT, dist1toN[t]) # 1 -> 片側未定テレポータの確定している方までの距離
    distNtoT = min(distNtoT, distNto1[t]) # N -> 片側未定テレポータの確定している方までの距離

  for i in range(1, N+1):
    if T:
      ans0 = dist1toN[N]
      ans1 = min(dist1toT + 1 + distNto1[i], dist1toN[i] + 1 + distNtoT)
      ans2 = dist1toT + 1 + 1 + distNtoT
      ans = min(ans0, ans1, ans2)
    else:
      ans = dist1toN[N]
    
    if ans < INF:
      print(ans)
    else:
      print(-1)


def bfs(G, v_start, dist, INF=10**9):
  nx = collections.deque([v_start])
  dist[v_start] = 0
  while nx:
    v_from = nx.popleft()
    for v_to in G[v_from]:
      if dist[v_to]==INF:
        dist[v_to] = dist[v_from] + 1
        nx.append(v_to)
  return dist


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