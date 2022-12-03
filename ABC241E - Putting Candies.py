n, k = map(int, input().split())
a = list(map(int, input().split()))

# 皿にX個のアメがあるとき、1回の操作でA[X%N]個のアメがもらえる
# (皿のアメの個数)%Nの状態から2^i回操作後にもらえるアメの総数をダブリングで求める
dp = [[0]*n for _ in range(41)]
for j in range(n): dp[0][j] = a[j]

for i in range(1, 41):
    for j in range(n):
        # ある余りjに対して、2^iのときにもらえる個数は
        # jから2^(i-1)操作してもらえる個数 = dp[i-1][j] に、
        # 元々の余りにそれを足したあと、さらに2^(i-1)回操作してもらえる個数、
        # すなわち j + dp[i-1][j] の余りから2^(i-1)回操作してもらえる個数
        # dp[i-1][ (j + dp[i-1][j]) % N ] を足したもの
        dp[i][j] = dp[i-1][j] + dp[i-1][(dp[i-1][j]+j)%n]

# 答えを求める
ans = 0
rem = 0
for i in range(41):
    if k & 2**i:
        ans += dp[i][rem]
        rem = ans%n

print(ans)