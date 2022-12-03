n, m, k = map(int ,input().split())

ans = 0
MOD = 998244353
dp = [[0]*k for _ in range(n)]
for j in range(min([m, k])):
    dp[0][j] = 1

for i in range(n-1):
    for j in range(k):
        for l in range(1, m+1):
            if j + l <= k-1:
                dp[i+1][j+l] += dp[i][j] % MOD

for j in range(k):
    ans += dp[n-1][j] % MOD

print(ans%MOD)