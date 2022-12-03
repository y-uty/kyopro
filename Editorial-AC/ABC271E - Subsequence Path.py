import sys
n, m, k = map(int, input().split())

roads = [(-1, -1, -1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    roads.append((a, b, c))

e = list(map(int, input().split()))

# dp[i][j]:= E1~Eiまでの部分列となる道の辿り方で都市jに着くときのMin
# 道路iを選ぶとき from: Ai, to: Bi でdp[i][Bi] = min(dp[i-1][Bi], dp[i-1][Ai]+Ci) となる
# 1つ前のAi, Biを見てBiを更新するので、i回ループ方向の配列を持つ必要がなく、
# 都市数ぶんの配列を、数列Eの長さ(K)回更新すればOK

INF = 10**18
# Eiまでの部分列で都市1 -> Biの移動が不可能なとき、良い経路として選ばれることはないので、
# 未達と同様に扱って、統一してINFで初期化し、遷移でminを取っていけばOK
dp = [INF]*(n+1)
dp[1] = 0

for i in range(k):
    ei = e[i]
    ai, bi, ci = roads[ei]

    dp[bi] = min(dp[bi], dp[ai]+ci)

if dp[n] < INF:
    print(dp[n])
else:
    print(-1)
