n = int(input())
a = list(map(int ,input().split()))

dp = [[0]*10 for _ in range(n-1)]
MOD = 998244353

f = (a[0] + a[1]) % 10
g = (a[0] * a[1]) % 10
dp[0][f] += 1
dp[0][g] += 1

for i in range(1, n-1):
    for j in range(10):
        if dp[i-1][j] > 0:
            f = (j + a[i+1]) % 10
            g = (j * a[i+1]) % 10
            dp[i][f] = (dp[i][f] + dp[i-1][j]) % MOD
            dp[i][g] = (dp[i][g] + dp[i-1][j]) % MOD   

for ans in dp[-1]:
    print(ans)