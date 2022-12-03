n,m,k = map(int, input().split())

dp = [[0]*(m+1) for _ in range(n+1)]
dp[1] = list(range(m+1))

MOD = 998244353

if k==0:
    ans = 1
    for _ in range(n):
        ans = (ans*m)%MOD
    print(ans)
    exit()

for i in range(2, n+1):
    for j in range(1, m+1):
        r = m - (j+k-1)
        if r > 0:
            vr = dp[i-1][m] - dp[i-1][j+k-1]
        else:
            vr = 0

        l = j-k
        if l > 0:
            vl = dp[i-1][j-k]
        else:
            vl = 0
        
        dp[i][j] = (dp[i][j-1] + vr + vl)%MOD

print(dp[n][m]%MOD)