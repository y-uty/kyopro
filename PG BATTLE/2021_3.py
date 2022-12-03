N, M, A, B = map(int, input().split())


# (0, 0) -> (N, M)
dp = [[0]*(N+1) for _ in range(M+1)]
dp[0][0] = 1

MOD = 998244353
for y in range(M+1):
    for x in range(N+1):

        if x+1 <= N:
            if (y, x+1) == (B, A):
                dp[y][x+1] = 0
            else:
                dp[y][x+1] += dp[y][x]
                dp[y][x+1] %= MOD
        
        if y+1 <= M:
            if (y+1, x) == (B, A):
                dp[y+1][x] = 0
            else:
                dp[y+1][x] += dp[y][x]
                dp[y+1][x] %= MOD

print(dp[M][N])

# for i in range(M+1):
#     print(dp[i])