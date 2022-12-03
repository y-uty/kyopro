import sys
import collections
sys.setrecursionlimit(10**9)
n = int(input())
tr = collections.defaultdict(list)
for _ in range(n-1):
    u, v, w = map(int, sys.stdin.readline().split())
    tr[u].append([w, v])
    tr[v].append([w, u])

colored = [-1]*(n+1)
# 始点はどこでもよいので1とする
vx = [[0, 1]]
c_evod = 0

# 木をdfsで探索し、そこまでの累積距離の偶奇によって塗り分けを決める.
# 偶数を白:0、奇数を:1 と決める(mod2の結果と一致して直感的なので).
# 始点から深さ順に塗り分けていくことで、自然に問題の条件を満たすことができる.
# ev+ev=ev ev+od=od, od+od=ev, od+ev=od からこれが成り立つ.
def dfs(v_from, c_transit, c_sofar):

    c_sofar += c_transit # 深さ1潜ったら距離加算
    colored[v_from] = 1 if c_sofar%2 else 0 #　偶奇で塗り分け

    for cv in tr[v_from]:
        ct, vt = cv
        if colored[vt] < 0: # 未到達なら次の深みへ
            dfs(vt, ct, c_sofar)

    c_sofar -= c_transit # 上に戻ったら距離減算

dfs(1, 0, 0)

print(*colored[1:], sep='\n')