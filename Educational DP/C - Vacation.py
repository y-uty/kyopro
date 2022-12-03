N = int(input())

# [i日目][A or B or Cを選んだとき]
dp = [0][0] 

for i in range(N):
    a, b, c = list(map(int, input().split()))
    today = []
    
    dp[i+1][0] = max([dp[i][1]+a, dp[i][2]+a])
    dp[i+1][1] = max([dp[i][0]+b, dp[i][2]+b])
    dp[i+1][2] = max([dp[i][0]+c, dp[i][1]+c])

print(max(dp[-1]))
