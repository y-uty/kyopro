N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [0] * N # i番目までの最小コストが確定したら代入していく

for i in range(1, N):
    mincost = float('inf')
    # いくつ先まで一度にいけるかが未定(K)なのでK回ループで調べる
    # ただし、ジャンプ先iがKより小さい場合はi回しかループできない
    for j in range(1, min([K, i])+1):
        mincost = min([mincost, dp[i-j] + abs(H[i-j] - H[i])])
    dp[i] = mincost

print(dp[-1])
