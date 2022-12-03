import sys
h, n = map(int, input().split())
magic = [[-1, -1]]
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    magic.append([a, b]) # 与ダメージ, 消費MP

dp = [[10**8]*(h+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    damage, mp = magic[i]
    dp[i][0] = 0

    for j in range(h): # 敵のHP-1まででよい
        if j<damage: # 魔法iを1回使った与ダメ未満は、そのままおろす
            dp[i][j] = dp[i-1][j]
        
        k = min([j+damage, h])
        x = dp[i][j] + mp
        y = dp[i-1][k]
        z = dp[i][k]
        dp[i][k] = min([x, y, z])

ans = 10**8
for i in range(1, n+1):
    if dp[i][-1] < ans:
        ans = dp[i][-1]

print(ans)