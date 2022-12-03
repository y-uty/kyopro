N = int(input())

# 'A': 0, 'C': 1, 'G': 2, 'T': 3
ACGT = ['A', 'C', 'G', 'T']
MOD = 10**9+7

# dp[i][j][k][l]:= 末尾から1文字目がj, 2文字目がk, 3文字目がl のときのi文字の文字列の通り数
# NGパターンは、AGC, ACG, GAC, AGxC, AxGC の5つ
# これを作らないように配るdpで遷移する
dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
for j in range(4):
  for k in range(4):
    for l in range(4):

        if ACGT[l]+ACGT[k]+ACGT[j] in ("AGC", "ACG", "GAC"):
          continue
        else:              
          dp[3][j][k][l] = 1

for i in range(3, N):
  for j in range(4):
    for k in range(4):
      for l in range(4):
      
        if dp[i][j][k][l] >= 0:
          # Aを選ぶ
          dp[i+1][0][j][k] += dp[i][j][k][l]
          dp[i+1][0][j][k] %= MOD

          # Cを選ぶ
          if not ((k==0 and j==2) or (k==2 and j==0) or (l==0 and k==2) or (l==0 and j==2)):
            dp[i+1][1][j][k] += dp[i][j][k][l]
            dp[i+1][1][j][k] %= MOD         

          # Gを選ぶ
          if not (k==0 and j==1):
            dp[i+1][2][j][k] += dp[i][j][k][l]
            dp[i+1][2][j][k] %= MOD        

          # Tを選ぶ
          dp[i+1][3][j][k] += dp[i][j][k][l]
          dp[i+1][3][j][k] %= MOD

ans = 0
for j in range(4):
  for k in range(4):
    for l in range(4):
      ans += dp[N][j][k][l]
      ans %= MOD

print(ans)