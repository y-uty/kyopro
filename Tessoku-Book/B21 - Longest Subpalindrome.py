n = int(input())
s = list(input())


# dp[l][r]:= l~r文字目の部分文字列で作れる回分の長さの最大値    
dp = [[-1]*(n+1) for _ in range(n+1)]

# 回文は、奇数長さ(中央がなんでもよい), 偶数長さ(すべて対称)がある
# 回文長が増えるのは dp[l-1][r-1] -> d[l][r] で S[l]=S[r] のときで、
# 必ず2ずつ増える、すなわち偶奇は変わらない
# したがって、初期状態として1文字, 連続する同じ2文字を定めておく

# 1文字だけは明らかに回文
for i in range(1, n+1):
    dp[i][i] = 1

# 連続する2文字が同じであれば回文, そうでなければ1文字
for i in range(1, n):
    if s[i-1]==s[i]:
        dp[i][i+1] = 2
    else:
        dp[i][i+1] = 1

# k=r-lを固定して、kの小さい方からdp
for k in range(2, n):
    for l in range(1, n-k+1):
        r = k+l

        # S[l]=S[r]のとき、回文長が2増える
        if s[l-1]==s[r-1]:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1], dp[l+1][r-1]+2)
        else:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1])

print(dp[1][n])
