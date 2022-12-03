H, W = map(int, input().split())
masu = [ list(input()) for _ in range(H) ]
MOD = 10**9+7

# 一度に一方向にどれだけでも移動できるので、
# 今いるマスの上/左/左斜め上の3方向背後にある全てのマスについて
# それらのマスに到達する通り数の総和が、今いるマスに到達する通り数となる
# よって、上/左/左斜め上それぞれで累積和を取りながらDPすればよい
dp = [[0]*W for _ in range(H)]
dp[0][0] = 1

# 左からの累積
LC = [[0]*W for _ in range(H)]
LC[0][0] = 1
# 上からの累積
UC = [[0]*W for _ in range(H)]
UC[0][0] = 1
# 左斜め上からの累積
LU = [[0]*W for _ in range(H)]
LU[0][0] = 1

# 遷移: dp[i][j] = LC[i-1][j] + UC[i][j-1] + LU[i-1][j-1]
for i in range(H):
    for j in range(W):

        if masu[i][j]=='.':
            x, y, z = 0, 0, 0
            if i-1 >= 0:
                x += UC[i-1][j]
            if j-1 >= 0:
                y += LC[i][j-1]
            if i-1 >= 0 and j-1 >= 0:
                z += LU[i-1][j-1]

            dp[i][j] = (dp[i][j] + (x+y+z))%MOD

            UC[i][j] = (x + dp[i][j])%MOD
            LC[i][j] = (y + dp[i][j])%MOD
            LU[i][j] = (z + dp[i][j])%MOD

        else:

            LC[i][j] = 0
            UC[i][j] = 0
            LU[i][j] = 0

print(dp[-1][-1])