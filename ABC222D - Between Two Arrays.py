n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 998244353

w = b[-1]+1
dp = [[0]*(w+1) for _ in range(n)]

for x in range(a[0], b[0]+1):
    dp[0][x] = 1

for i in range(n-1):

    for j in range(a[i], b[i]+1):
        dp[i+1][max([a[i+1], j])] += dp[i][j] % MOD
        dp[i+1][b[i+1]+1] -= dp[i][j] % MOD

    for k in range(w):
        dp[i+1][k+1] += dp[i+1][k] % MOD

print(sum(dp[-1])%MOD)