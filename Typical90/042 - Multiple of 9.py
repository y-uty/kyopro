k = int(input())
MOD = 10**9+7

# dp[i][j]:= 桁和がiで9で割った余りがjとなるような数がいくつあるか
# mod9がaの数の末尾にxを足すと、そのmod9は(10*a+x)%9
# 桁和はそのままxを加算していけばいいので、dp[i][j]に対してx=1~9で遷移すれば解ける
# 状態はN<=10^5と余り0~8, 遷移が9通りなので、計算量は10^7未満

dp = [[0]*9 for _ in range(k+1)]
for i in range(1, min([k+1, 10])):
    dp[i][i%9] = 1

for i in range(1, k):
    for j in range(9):
        if dp[i][j] > 0:
            for x in range(1, 10): # 末尾に足す数字1~9
                if i+x <= k:
                    j_next = (10*j+x)%9
                    dp[i+x][j_next] += dp[i][j]
                    dp[i+x][j_next] %= MOD

# 桁和がKで、9で割った余りが0となる通り数が答え
print(dp[k][0]%MOD)