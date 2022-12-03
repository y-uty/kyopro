n, p, k = map(int, input().split())
A = []
for _ in range(n):
    arow = list(map(int, input().split()))
    A.append(arow)

# 全点対最短コストはWarshall-Floyd法で求める
INF = 10**18
def is_ok(x):
    dp = [[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = A[i][j] if A[i][j] >= 1 else x

    for m in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][m]+dp[m][j])
    
    # 最短コストP以下の点対の個数を調べる
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            cnt += 1 if dp[i][j] <= p else 0
    
    # その個数がK個以下かどうか
    return True if cnt <= k else False


# 二分探索で最短コストP以下の点対の個数がK個以下となる最小のXを求める

# 最小値？ -> (ng, ok], 最大値？ -> [ok, ng) を渡す.
ng, ok = 0, 10**18
def bin_srch_mgr(ok, ng):
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if is_ok(mid): ok = mid
        else: ng = mid
    return ok

xmin_at_k = bin_srch_mgr(ok, ng)

# K-1個以下となる最小のXも求める
k -= 1
ng, ok = 0, 10**18
xmin_at_km1 = bin_srch_mgr(ok, ng)
k += 1

#print(xmin_at_k, xmin_at_km1)
if xmin_at_k==10**18:
    print(0)
    exit()

if xmin_at_km1==10**18:
    print('Infinity')
    exit()

# K個以下となる最小のXが、ちょうどK個になるかを確かめる
dp = [[INF]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dp[i][j] = A[i][j] if A[i][j] >= 1 else xmin_at_k

for m in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][m]+dp[m][j])

# 最短コストP以下の点対の個数を調べる
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        cnt += 1 if dp[i][j] <= p else 0

if cnt==k:
    print(xmin_at_km1 - xmin_at_k)
else:
    print(0)