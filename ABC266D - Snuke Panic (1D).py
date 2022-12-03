import sys
import collections
n = int(input())
snuke = collections.defaultdict(list)
for _ in range(n):
    t, x, a = map(int, sys.stdin.readline().split())
    snuke[t] = [x, a]
    maxt = t  

dp = [[-1]*5 for _ in range(maxt+1)]
dp[0][0] = 0

tsum = 0
for i in range(1, maxt+1):

    pt = [0]*5
    if snuke[i]:
        x = snuke[i][0]
        a = snuke[i][1]
        pt[x] = a

    for j in range(5):

        # その場に留まる
        tmp1 = -1 if dp[i-1][j]==-1 else dp[i-1][j]+pt[j]

        # 左から移動してくる
        if j==0:
            tmp2 = -1
        elif dp[i-1][j-1]==-1:
            tmp2 = -1
        else:
            tmp2 = dp[i-1][j-1] + pt[j]

        # 右から移動してくる
        if j==4:
            tmp3 = -1
        elif dp[i-1][j+1]==-1:
            tmp3 = -1
        else:
            tmp3 = dp[i-1][j+1] + pt[j]

        dp[i][j] = max([tmp1, tmp2, tmp3])

print(max(dp[-1]))