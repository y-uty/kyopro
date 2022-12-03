n = int(input())
s = []
for _ in range(n):
    s.append(str(input()))

dp = [[0]*2 for _ in range(n+1)]
dp[0][0] = 1 # True
dp[0][1] = 1 # False

for i in range(n):
    
    and_or = s[i]

    if and_or == 'AND':
        # True -(AND)-> True/False
        dp[i+1][0] += dp[i][0]
        dp[i+1][1] += dp[i][0]

        # False -(AND)-> False/False
        dp[i+1][1] += 2 * dp[i][1]

    elif and_or == 'OR':
        # True -(OR)-> True/True
        dp[i+1][0] += 2 * dp[i][0]

        # False -(OR)-> True/False
        dp[i+1][0] += dp[i][1]
        dp[i+1][1] += dp[i][1]

print(dp[-1][0])