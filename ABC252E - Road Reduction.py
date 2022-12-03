import sys
import collections
import heapq

n, m = map(int, input().split())
roads = collections.defaultdict(list)
ans = [] # 保守する道路=MSTを作る辺の番号
cand = [] # 選ぶ辺の候補(heap)
seen_check = [False]*(n+1)
seen_check[1] = True
seen_count = 1 # 頂点1は到達済み
c_sofar = 0 # 時点最短コスト
for i in range(1, m+1):
    a, b, c =  map(int, sys.stdin.readline().split())
    roads[a].append([c, b, i])
    roads[b].append([c, a, i])
    if a==1: heapq.heappush(cand, [c, b, i])
    if b==1: heapq.heappush(cand, [c, a, i])

# Prim法 (頂点1からスタート); AC後メモ - 最短経路木をつくる
while seen_count < n: # 全ての頂点に到達するまで
    min_chosen = heapq.heappop(cand)
    c_to, v_to, e_num_to = min_chosen

    # 到達済みの場合は追加しない
    if seen_check[v_to]:
        continue

    # MSTに辺を追加
    ans.append(e_num_to)
    # 時点最短コスト
    c_sofar = c_to
    seen_count += 1
    seen_check[v_to] = True
    
    # 到達先から伸びる(MSTを作る候補の)辺を追加
    for next_cand in roads[v_to]:
        c_next, v_next, e_num_next = next_cand
        # 到達済みの場合は追加しない
        if seen_check[v_next]:
            continue
        # 時点最短コスト+その辺のコストとして、MST辺の候補に追加
        heapq.heappush(cand, [c_next+c_sofar, v_next, e_num_next])

# 選択した辺の出力
print(*ans)