N, X = map(int, input().split())

# 0~Nまでと0~Xまでの(N+1)*(X+1)のテーブルを使う
dp = [[0]*(X+1) for _ in range(N+1)]
dp[0][0] = 1

# i回目のジャンプで到達しうるjについて、dp[i][j] = 1とする
# dp[N][X] = 1 であればOK。X>10の場合はスキップ
for i in range(N):
    a, b = map(int, input().split())
    for j in range(X):
        if dp[i][j] == 1:
            if j+a <= X:
                dp[i+1][j+a] = 1
            if j+b <= X:
                dp[i+1][j+b] = 1

print("Yes" if dp[N][X]==1 else "No")