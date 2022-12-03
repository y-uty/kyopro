n = int(input())
t = list(map(int, input().split()))
tsum = sum(t)

# t[i]の組でjが作れる場合に1を立てるdpテーブル
dp = [[0]*(tsum+1) for _ in range(n+1)]

for i in range(1, n+1):
    # 自分t[i]のみを選ぶケースについてまず1を立てる
    dp[i][t[i-1]] = 1
    for j in range(1, tsum+1):
        # t[i-1]で登場済みの場合、
        if dp[i-1][j]:
            # そのまま1を下ろして、
            dp[i][j] = dp[i-1][j]
            # そこにt[i]を足したjも1を立てる
            dp[i][j+t[i-1]] = 1

# sum(t)/2が最適で、そうならない場合は
# t[i]の組み合わせで作りうる数のうち、sum(t)/2より大きい最小値を選ぶ
import math
best = math.ceil(tsum / 2)
# dp[-1][tsum]までに必ず候補があるので、見つけたら答えを出力して終了
for k in range(best, tsum+1):
    if dp[-1][k]:
        print(k)
        exit()