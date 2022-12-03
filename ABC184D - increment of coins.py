a, b, c = map(int, input().split())

# dp[i][j][k]:= 金貨i枚、銀貨j枚、銅貨k枚の状態になる確率
# 各硬貨の上限が100枚なので、状態は10*6
# 各状態からいずれかの硬貨が+1枚するので、遷移は3通り

# dp[i][j][k]からdp[i+1][j][k]にいく確率は、dp[i][j][k] * (i / i+j+k)
# 同一のdp[i][j][k]への経路は互いに排反なので、たどり着くたびに和をとるので、
# dp[i+1][j][k] += dp[i][j][k] * (i / i+j+k)
# j+1, k+1の場合も同様

# 複数の硬貨が100枚になることはないので、dpテーブルを埋め終わったら
# dp[100][j][k], dp[i][100][j], dp[i][j][100] に入っている確率が、求める期待値の元情報
# 期待値を求めるのに必要な試行回数は、i+j+k - (初期状態の枚数の総和) である

dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
dp[a][b][c] = 1

init_coins = a+b+c

for i in range(a, 100):
    for j in range(b, 100):
        for k in range(c, 100):
            cnt_all_coins = i+j+k
            pi = i/cnt_all_coins
            pj = j/cnt_all_coins
            pk = k/cnt_all_coins
            
            dp[i+1][j][k] += dp[i][j][k] * pi
            dp[i][j+1][k] += dp[i][j][k] * pj
            dp[i][j][k+1] += dp[i][j][k] * pk

ans = 0

# dp[100][j][k]
for j in range(b, 100):
    for k in range(c, 100):
        ans += dp[100][j][k] * (100+j+k - init_coins)

# dp[i][100][k]
for i in range(a, 100):
    for k in range(c, 100):
        ans += dp[i][100][k] * (i+100+k - init_coins)

# dp[i][j][100]
for i in range(a, 100):
    for j in range(b, 100):
        ans += dp[i][j][100] * (i+j+100 - init_coins)
    
print(ans)