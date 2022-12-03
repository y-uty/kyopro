import sys
n, q = map(int, input().split())
a = list(map(int, input().split()))

# ダブリングで位置jの2^i日後の位置を前計算しておく
dp = [[0]*(n+1) for _ in range(31)]
for j in range(n): dp[0][j+1] = a[j]

for i in range(1, 31):
    for j in range(1, n+1):
        # jの2^iあとの位置 = (jの2^(i-1)あとの位置)の2^(i-1)あとの位置
        dp[i][j] = dp[i-1][dp[i-1][j]]

# クエリ処理
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())

    # Yの、2^iのビットが立っているところだけ、2^i日後に進む
    for i in range(31):
        if y & 2**i:
            x = dp[i][x]

    print(x)