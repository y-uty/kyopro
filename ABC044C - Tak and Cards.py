n, a = map(int, input().split())
x = list(map(int, input().split()))
maxk = sum(x)

# dp[i][j][k] := i枚目まででj枚選んだときの合計がkである通り数
# 状態数 N*N*sum(X) -> O(N^3*max(X)), 遷移O(1)
# 枚数がjで平均がAになるのは、合計がA*jのときなので、
# 答えは sum(dp[N][j][A*j])
dp = [[[0]*(maxk+1) for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    # xiで初めて選ぶ
    dp[i+1][1][x[i]] += 1
    for j in range(n):
        for k in range(maxk+1):
            if dp[i][j][k] > 0:
                # i+1枚目を選ばない
                dp[i+1][j][k] += dp[i][j][k]
                # i+1枚目を選ぶ
                dp[i+1][j+1][k+x[i]] += dp[i][j][k]

ans = 0
for j in range(1, n+1):
    k = a*j
    if k > maxk: continue
    ans += dp[n][j][k]

print(ans)
