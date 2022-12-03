import sys
import collections
n, m, k, s, t, x = map(int, input().split())
G = collections.defaultdict(list)
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

ans = 0
MOD = 998244353
# dp[m][i][j]:= i項めがjで、それまでのXの登場回数%2がmである通り数
# 答えはdp[0][K][T]
dp = [[[0]*(n+1) for _ in range(k+1)] for _ in range(2)]
dp[0][0][s] = 1

for i in range(k):

    for j in range(1, n+1):

        for m in range(2):

            if dp[m][i][j] > 0:

                for v_to in G[j]:
                    m_next = m^1 if v_to == x else m
                    dp[m_next][i+1][v_to] = (dp[m_next][i+1][v_to] + dp[m][i][j])%MOD

print(dp[0][k][t])