n = int(input())
cities = []
for _ in range(n):
    x, y, z = map(int, input().split())
    cities.append((x, y, z))

def dist(a,b,c,p,q,r):
    return abs(p-a) + abs(q-b) + max(0, r-c)

INF = 10**18
dp = [[INF]*(n+1) for _ in range(2**n)]
dp[1][1] = 0

# シンプルな(2^N*N^2)だとN>=16が間に合わないので、不要な移動は削る
for i in range(1, 2**n):
    # 訪問済み集合iから、整数のリストとして取り出す
    visited, notyet = [], []
    for e in range(n):
        if i & 2**e: visited.append(e+1)
        else: notyet.append(e+1)

    for j in visited: # fromは訪問済みのみ
        for k in notyet: # toは未訪問のみ
            dp[i | 1<<(k-1)][k] = min(dp[i | 1<<(k-1)][k], dp[i][j]+dist(*cities[j-1], *cities[k-1]))

ans = INF
# 最後に都市2~Nから1への移動を計算して最小値が答え
for i in range(2, n+1):
    ans = min(ans, dp[2**n-1][i] + dist(*cities[i-1], *cities[1-1]))
print(ans)