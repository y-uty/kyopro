s = list(input())
n = len(s)

# 各マスのこどもを左から1~Nとして、
# 2^k回移動後にこどもがどこにいるかをダブリングで求める

# N回移動すれば必ず最終局面に到達するが、
# 移動回数の偶奇によって2種類の状態がある
# 10^100は偶数なので、Nより大きな適当な2^k回移動後の情報から解答すればOK

dp = [[-1]*n for _ in range(20)]
for j in range(n):
    # 1回目の移動はSを元に
    if s[j]=='R':
        dp[0][j] = j+1
    else:
        dp[0][j] = j-1

# ダブリングテーブルを埋める
for i in range(1, 20):
    for j in range(n):
        # jの2^iあとの位置 = (jの2^(i-1)あとの位置)の2^(i-1)あとの位置
        dp[i][j] = dp[i-1][dp[i-1][j]]

# こどもがいる位置 -> 位置ごとのこどもの人数に変換
ans = [0]*n
for j in range(n): ans[dp[-1][j]] += 1

print(*ans)