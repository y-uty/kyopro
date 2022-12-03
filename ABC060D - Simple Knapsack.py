n, w_all = map(int, input().split())
items = []
w1 = 0
for i in range(n):
    wi, vi = map(int, input().split())
    if i==0: w1 = wi
    items.append((wi, vi))

# dp[i][j][k] := i番目までのモノからk個選んで重さw1*k+jとなるときの価値の最大値
dp = [[[-1]*(n+1) for _ in range(3*n+1)] for _ in range(n+1)]
dp[0][0][0] = 0

for i in range(n):
    wnow, vnow = items[i]

    for j in range(3*n+1):

        for k in range(n):

            if dp[i][j][k] >= 0:
                # 選ばない
                dp[i+1][j][k] = max(dp[i][j][k], dp[i+1][j][k])

                # 選ぶ
                w_add = wnow - w1
                dp[i+1][j+w_add][k+1] = max(dp[i][j][k]+vnow, dp[i+1][j+w_add][k+1])

ans = 0
for i in range(n+1):
    for j in range(3*n+1):
        for k in range(n+1):
            if k*w1+j <= w_all:
                if dp[i][j][k] > ans: ans = dp[i][j][k]

print(ans)