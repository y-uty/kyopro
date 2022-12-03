n, m = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j]:= i番目までの中でj個選んだときのMax
dp = [[-10**18]*(m+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):

    # Aiで、1こめを選ぶ
    dp[i+1][1] = a[i]

    for j in range(m+1):

        # Aiを選ばない
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        # Aiを選ぶ
        if j < m:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+a[i]*(j+1))

print(dp[n][m])
