import sys
import collections
import heapq
n, m = map(int, sys.stdin.readline().split())
G = collections.defaultdict(list)
deg = collections.defaultdict(int) # 各頂点の入次数を管理

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    deg[b] += 1

# トポロジカルソート
tpsorted = []
vx_deg0 = []
# 辞書順最小にするために、入次数0の中からheapqで最小を取り出す
for i in range(1, n+1):
    if deg[i]==0:
        heapq.heappush(vx_deg0, i)

while vx_deg0:
    v_del = heapq.heappop(vx_deg0)
    # 取り出した入次数0の頂点はソート済みとしてリストに保存
    tpsorted.append(v_del)

    for v_adj in G[v_del]:
        # 削除した入次数0の頂点が向いている先の頂点の入次数を1減らす
        deg[v_adj] -=1
        # その結果、入次数0になった頂点はheapqに追加
        if deg[v_adj]==0:
            heapq.heappush(vx_deg0, v_adj)

# ソート済み頂点数と全頂点数が同じであればソート可能・完了
if len(tpsorted)==n:
    print(*tpsorted)
else:
    print(-1)