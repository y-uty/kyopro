import sys
import collections
sys.setrecursionlimit(10**7)
n = int(input())
tr = collections.defaultdict(list)
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    tr[u].append(v)
    tr[v].append(u)

anslist = [0]*(n+1)
subtr_size = [0]*(n+1)
cost = [0]*(n+1)
# まず、頂点1を根として普通にDFSしてsum(dist(1, j))を求める
# このとき、帰りがけに各頂点を根とした部分木の大きさも求める

visited = [False]*(n+1)
def dfs(v_from, cnt, dist):
    visited[v_from] = True

    tmp = 1 # 部分木頂点数のカウント
    for v_to in tr[v_from]:
        if not visited[v_to]:

            dist += 1
            # 再帰を抜けるときに、自分より下の頂点数を足し合わせる
            tmp += dfs(v_to, cnt, dist)
            dist -= 1

    subtr_size[v_from] = tmp
    cost[v_from] = dist

    return tmp

dfs(1, 0, 0)

anslist[1] = sum(cost)

# 頂点1に隣接する頂点から順番にBFSでsum(dist(k, j))を計算する
nx = collections.deque([1])
visited = [False]*(n+1)
visited[1] = True
while nx:
    v_from = nx.popleft()

    for v_to in tr[v_from]:
        if not visited[v_to]:
            # 頂点jが根kの部分木に含まれるとき、dist(k, j)は1ずつ減る -> -1*部分木kの大きさ
            # そうでないとき、dist(k, j)は1ずつ増える -> +1*(N-部分木kの大きさ)
            anslist[v_to] = anslist[v_from]+(n-subtr_size[v_to])-subtr_size[v_to]
            visited[v_to] = True
            nx.append(v_to)

print(*anslist[1:], sep='\n')
