n, m = map(int, input().split())

if m == 0:
    print(1)
    exit()

import collections
f = collections.defaultdict(set)
v = set()

import sys
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    f[a].add(b)
    f[b].add(a)
    v.add(a)
    v.add(b)

costs = [n]*(n+1)

# 各連結成分の中にノードがいくつあるかを数えるdict
l = collections.defaultdict(int)

# 通常bfsで最短コストを記録しながら、通過したノード数を数えていく
def bfs(v_stt, num_g):
    q = collections.deque()
    q.append(v_stt)
    l[num_g] += 1
    costs[v_stt] = 0

    while q:
        v_from = q.popleft()
        nexts = list(f[v_from])

        for v_next in nexts:
            tmp_mincost = costs[v_from] + 1
            if costs[v_next] > tmp_mincost:
                costs[v_next] = tmp_mincost
                q.append(v_next)
                l[num_g] += 1

# 入力のa, bの集合をリストに戻して、bfs始点のリストとする
v = list(v)
num_g = 1
for x in v:
    # 始点候補のノードがコスト未計算であれば、未処理の連結成分であるためbfs処理に突入する
    if costs[x] == n:
        bfs(x, num_g)
        num_g += 1

# 連結成分ごとのノード数の最大値が答え
print(max(l.values())) # dictが空だとエラーとなるため、冒頭でm=0の例外処理を記述した