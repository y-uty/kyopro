import sys
r, c, k = map(int, input().split())
goods = [[0]*c for _ in range(r)]
for _ in range(k):
    ro, co, v = map(int, sys.stdin.readline().split())
    goods[ro-1][co-1] = v

# dp[i][j][m] = i行目, j列目にいて、i行目でm個のアイテムを拾ったときのMax
# 遷移: (↓ or →) × (アイテムがあるとき、とる(m+1) or とらない(m))
dp = [[[0]*c for _ in range(r)] for _ in range(4)]
dp[0][0][0] = 0
dp[1][0][0] = goods[0][0]

for i in range(r):
    for j in range(c):
        for m in range(4):

            # 下へ移動するとき、mは一旦リセットされる
            if i+1 < r:
                # 拾わない
                dp[0][i+1][j] = max(dp[0][i+1][j], dp[m][i][j])
                # アイテムがある場合は拾う遷移
                dp[1][i+1][j] = max(dp[1][i+1][j], dp[m][i][j]+goods[i+1][j])

            # 右へ移動するとき、アイテムを拾えるのはm=0~2のみ
            if j+1 < c:
                # 拾わない
                dp[m][i][j+1] = max(dp[m][i][j+1], dp[m][i][j])
                # アイテムがある場合は拾う遷移
                if m <= 2:
                    dp[m+1][i][j+1] = max(dp[m+1][i][j+1], dp[m][i][j]+goods[i][j+1])

print(max(dp[0][-1][-1], dp[1][-1][-1], dp[2][-1][-1], dp[3][-1][-1]))