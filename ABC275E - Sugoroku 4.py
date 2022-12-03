N, M, K = map(int, input().split())
MOD = 998244353
# 逆元の前計算; 遷移の度にlog p かけていると間に合わない
invM = pow(M, MOD-2, MOD)

# dp[i][j]:= i回ルーレットをまわしてjにいる確率
# 状態 K*N, 遷移 M
dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][0] = 1
for i in range(K):
    for j in range(N): # i<KでNに到達した場合はそれ以上考えなくて良い

        if dp[i][j] > 0:
            for k in range(1, M+1):
                nx = j+k
                if nx > N: nx = 2*N-nx # 折り返しの場合
                dp[i+1][nx] = (dp[i+1][nx] + dp[i][j]*invM)%MOD

# K回までいずれかでマスNに到達する確率を足し合わたものが答え
ans = 0
for i in range(K+1):
    ans = (ans+dp[i][N])%MOD

print(ans)