D, G = map(int, input().split())
problems = []
all_num = 0
for i in range(D):
    p, c = map(int, input().split())
    all_num += p
    problems.append((p, c)) # i点の問題数: p, コンプBonus: c

# dp[i][j]:= 100*i点の問題までで、合計j問選んだときの点数の最大値
dp = [[-1]*(all_num+1) for _ in range(D+1)]
dp[0][0] = 0

for i in range(D):

    pi, ci, = problems[i]

    for j in range(all_num):

        if dp[i][j] >= 0:

            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

            for k in range(pi):

                if k+1 < pi:
                    dp[i+1][j+(k+1)] = max(dp[i+1][j+(k+1)], dp[i][j]+100*(i+1)*(k+1))

                else:
                    dp[i+1][j+(k+1)] = max(dp[i+1][j+(k+1)], dp[i][j]+100*(i+1)*(k+1)+ci)

# for i in range(D+1):
#     print(dp[i])

for j in range(all_num+1):
    if dp[D][j] >= G:
        print(j)
        exit()