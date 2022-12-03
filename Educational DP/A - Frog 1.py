N = int(input())
H = list(map(int, input().split()))
dp = [] # i番目までの最小コストが確定したら追加していく

for i in range(N):
    if i == 0:
        dp.append(0)
    elif i == 1:
        dp.append(abs(H[0] - H[1]))
    else:
        dp.append(min([dp[i-1] + abs(H[i-1] - H[i]), dp[i-2] + abs(H[i-2] - H[i])]))

print(dp[-1])
