import sys
import collections
n, m = map(int, input().split())
x = [0] + list(map(int, input().split()))
bonus = collections.defaultdict(int)
for _ in range(m):
    c, y = map(int, sys.stdin.readline().split())
    bonus[c] = y

dp = [[0]*(n+1) for _ in range(n+1)]
dp[1][1] = x[1]+bonus[1]

for i in range(1, n):
    for j in range(n+1):
        if dp[i][j] > 0:

            dp[i+1][j+1] = max([dp[i+1][j+1], dp[i][j]+x[i+1]+bonus[j+1]])

    dp[i+1][0] = max(dp[i])

print(max(dp[-1]))