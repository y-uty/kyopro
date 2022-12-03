n, l = map(int, input().split())

# ある段数に到達する方法は、L段下から来るか、1段下から来るかの2通りある
# シンプルなもらうdpで解ける
# dp[i]:= dp[i-L] + dp[i-1] (i>=L)
# 1段ずつしか手段がないのでdp[i|i<L]=1で初期化する
# また、L<Nの場合、L段ジャンプは使えない

if n < l:
    print(1)
    exit()

dp = [0]*(n+1)
for i in range(l):
    dp[i] = 1

for i in range(l, n+1):
    dp[i] = dp[i-l]+dp[i-1]
    dp[i] %= 10**9+7

print(dp[-1])