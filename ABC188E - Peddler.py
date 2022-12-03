import sys
import collections
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
paths_from = collections.defaultdict(list)
paths_to = collections.defaultdict(list)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    paths_from[y].append(x) # fromの頂点リストを持っておく
    paths_to[x].append(y) # 行き先があるかチェックに使う

dp_buy = [0]*(n+1)
ans = -10**9
# dp_buy[i] := 町iまでに通った町で最も安い価格
# 町iで売ったときの利益をa[i]-dp_buy[i]で考える
for i in range(1, n+1):

    mincost_past = 10**9
    for v_from in paths_from[i]:
        past_buy = dp_buy[v_from]
        if past_buy < mincost_past: mincost_past = past_buy

    if len(paths_to[i])==0: # 最後の町で買うことはできない
        dp_buy[i] = mincost_past
    else: # 通ってきた町, 今いる町 のうち最安値
        dp_buy[i] = min(a[i], mincost_past)

    if len(paths_from[i])==0: # 最初の町で売ることはできない
        profit = -10**9
    else:
        profit = a[i]-dp_buy[i]

    if profit > ans: ans = profit

print(ans)