import sys

## 全点対最短経路(Warshall-Floyd法):O(頂点数N^3)
n, m = map(int, input().split())

# dp[k][i][j] := 頂点0〜kのみを使うときの頂点iから頂点jへの最短経路.
# 初期化: dp[0][i][j]は頂点i, jを直接結ぶ辺のコスト
# 結ぶ辺がない場合はINF. dp[i][i] = 0.
INF = 10**9
dp = [[INF]*(n+1) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    dp[a][b] = c

for i in range(1, n+1):
    dp[i][i] = 0

# 3重ループでdp[k][i][j]を更新していく
# dp[k][i][j] = min(dp[k-1][i][j] - ①, dp[i][k]+dp[k][j] - ②)
# ①: 頂点kを通らない場合 = 通らないならkを含めてもk-1まででも結果は変わらない
# ②: 頂点kを通る場合(i -> k + k -> j)
# ①は直前のkの値が使えるし、②はそのような辺がなければINFとなる.
# よって、kについては次元を持たず同じ配列を使いまわしながら更新できる.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][k]!=INF and dp[k][j]!=INF:
                # 頂点kに辿り着けないならskip. dp[i][j]はkを通らないならそのままでOK.
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
