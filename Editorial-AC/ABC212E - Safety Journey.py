import sys
import collections
n, m, k = map(int, input().split())
ng = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    ng[u].append(v)
    ng[v].append(u)

# dp[i][j]:= i日後に都市jにいる通り数
dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][1] = 1

MOD = 998244353
for i in range(1, k+1):
    # まず、通れないような道がない場合を考えると、同じ都市にはいられないので
    # dp[i][j] = sum(dp[i-1]) - dp[i-1][j] である
    # sumの部分は、iに対して先に求めておき、jごとにdp[i-1][j]を差し引く
    prev_day = sum(dp[i-1])%MOD

    for j in range(1, n+1):

        prev_day_j = prev_day - dp[i-1][j]

        # さらに、通れない道がある場合は、行き先jごとにそのぶんも差し引いていく
        # 1<=j<=N全体で2M回の計算で、iごとにO(N+M)の前処理が行われる
        for l in ng[j]:
            prev_day_j -= dp[i-1][l]
        
        # その結果を用いればO(1)で遷移できるから、
        # 全体でO((N+M)K)
        dp[i][j] = prev_day_j%MOD

print(dp[k][1])