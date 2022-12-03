import sys
import collections
sys.setrecursionlimit(10**7)
n = int(input())
tr = collections.defaultdict(list)
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tr[a].append(b)
    tr[b].append(a)

# 木は必ず二部グラフである
# よって、隣り合う頂点を異なる2色で塗り分けることが可能
# 塗り分けはDFSで行い、多く塗った方の色の頂点をちょうどN/2個出力すればよい

colored = [-1]*(n+1) # 色0/1で彩色する

cnt = [0, 0] # 色0/1でいくつの頂点を彩色したか？
# DFS処理
def dfs(v_from):

    for v_to in tr[v_from]:
        if colored[v_to] < 0:
            # fromの頂点と異なる色: 2色なのでxorで0/1反転
            # n>=3色なら+1%nで
            colored[v_to] = colored[v_from]^1
            cnt[colored[v_to]] += 1
            dfs(v_to)

# 適当な頂点からDFSで彩色
colored[1] = 0
dfs(1)

ans = []
# 半分以上を塗った方の色を選び、その色の頂点をN/2個まで出力
x = 0 if cnt[0]>cnt[1] else 1
for i in range(1, n+1):
    if colored[i]==x:
        ans.append(i)

print(*ans[:n//2])