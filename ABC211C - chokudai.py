s = str(input())

dp = [[0]*len(s) for _ in range(8)]

chokudai = 'iadukohc'
cnt = 0

for i in range(8):
    jlist = list(range(len(s)))
    jlist.sort(reverse=True)
    cnt = 0
    for j in jlist:
        if i == 0:
            if s[j] == chokudai[i]:
                cnt += 1
            dp[i][j] = cnt

        else:
            if dp[i-1][j] == 0:
                dp[i][j] = 0
            else:
                if s[j] == chokudai[i]: 
                    cnt += dp[i-1][j]
                    dp[i][j] += cnt
                    
                else:
                    dp[i][j] = cnt

print(dp[-1][0] % (10**9 + 7))