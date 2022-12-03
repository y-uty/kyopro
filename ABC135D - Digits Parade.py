s = str(input())
MOD = 10**9+7

# dp[i][j]:= Sの頭からi文字目までで作れる整数で、mod 13がjになるようなものの数
# 状態 |S|*13, 遷移 10, よって <= 1.3*10^7
dp = [[0]*13 for _ in range(len(s))]

# Sの1文字目
if s[0]=='?':
    for i in range(10):
        dp[0][i] += 1
else:
    i = int(s[0])
    dp[0][i] += 1

# Sの2文字目以降は、1文字前までのパターン数を持ち越していく
# 整数xの末尾にdを足すと、10x+dになるので、これの余りをとっていく
# 遷移 dp[i+1][新しい余り] += dp[i][元の整数(1文字前で求めた余り)]
# i+1文字目が'?'のときは0~9まで全て、そうでないときはその数字の場合のみで遷移する
for i in range(len(s)-1):
    for j in range(13):

        if dp[i][j] > 0:
            x = s[i+1]
            if x=='?':
                for k in range(10):
                    m = (10*j+k)%13
                    dp[i+1][m] = (dp[i+1][m]+dp[i][j])%MOD
            else:
                x = int(x)
                m = (10*j+x)%13
                dp[i+1][m] += (dp[i+1][m]+dp[i][j])%MOD

# |S|文字目まで考えた結果、mod13が5であるパターン数が答え
print(dp[-1][5])