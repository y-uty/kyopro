n = int(input())
P = [(0, 0)]
for _ in range(n):
    p, a = map(int, input().split())
    # i番目のブロックをPiより先に除くとAi点を得る
    P.append((p, a))

# dp[l][r]:= l~r番目のブロックが残っている状態での得点の最大値
dp = [[-1]*(n+1) for _ in range(n+1)]
dp[1][n] = 0

# ******* 初期状態
# ******- 右端から1つ除く
# -****** 左端から1つ除く
# *****-- 右端から2つ除く
# -*****- 右端から1つ, 左端から1つ除く
# --***** 左端から2つ除く
# ****---
# -****--
# --****-
# ---****
# ...となるようにループを回していく


for k in range(n-2, -1, -1):
    # k = r-l; 区間の長さを固定して、lを順番に. 長さとlが決まればrも決まる
    for l in range(1, n-k+1):
        r = k+l

        # dp[l][r] = dp[l-1][r]+(l-1番目のブロックを除く点数), dp[l][r+1]+(r+1番目のブロックを除く点数)
        if l > 1:
            cond_p, get_p = P[l-1]
            if cond_p < l or cond_p > r:
                get_p = 0
            scr1 = dp[l-1][r] + get_p
        else:
            scr1 = 0
        
        if r < n:
            cond_p, get_p = P[r+1]
            if cond_p < l or cond_p > r:
                get_p = 0
            scr2 = dp[l][r+1] + get_p
        else:
            scr2 = 0

        dp[l][r] = max(scr1, scr2)

ans = 0
for i in range(n):
    ans = max(ans, dp[i][i])           
print(ans)
