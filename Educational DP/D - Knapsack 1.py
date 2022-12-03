N, W = map(int, input().split())

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    weight, val = map(int, input().split())

    for j in range(W+1):
        if j >= weight:
            chosen = dp[i][j-weight] + val
            not_chosen = dp[i][j]
            dp[i+1][j] = max([chosen, not_chosen])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[-1][-1])