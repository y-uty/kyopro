import sys
n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
obst = set()
MOD = 998244353
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    cord = (x, y)
    obst.add(cord)

# ワープ1,2,3をそれぞれa,b,c回行ったとすると、合計a+b+c回のワープの中で、
# ワープをどのような順序で行ったに関係なく、同じ座標に到達する
# 従って、ある地点に到達する場合の数は、各ワープの回数だけで決まる

# dp[i][j][k]:= ワープ1,2,3をそれぞれi,j,k回行う場合の数
# i+j+k = N であるようなdp[i][j][k]の総和が答え
dp = [[[0]*(n+2) for _ in range(n+2)] for _ in range(n+2)]
dp[0][0][0] = 1

ans = 0

for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if i+j+k > n: continue

            x_now = a*i + c*j + e*k
            y_now = b*i + d*j + f*k

            if (x_now, y_now) in obst: continue

            tmp = dp[i][j][k]
            if i+j+k == n: ans = (ans+tmp)%MOD
            
            # 現在のワープ回数(i, j, k)から、(i+1, j, k), (i, j+1, k), (i, j, k+1)回に遷移する
            dp[i+1][j][k] = (dp[i+1][j][k] + tmp)%MOD
            dp[i][j+1][k] = (dp[i][j+1][k] + tmp)%MOD
            dp[i][j][k+1] = (dp[i][j][k+1] + tmp)%MOD

print(ans)
