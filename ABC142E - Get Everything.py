import sys
n, m = map(int, input().split())
keys = []

# 宝箱の数N<=12と小さいことに着目すると、
# 宝箱を開けた/開けてないを1/0のビットで表現すれば状態数は2^Nとなるから
# 遷移を鍵iを使う/使わないとしてO(2^N * M)のDPで解ける

# 入力で与えられる鍵の情報は、鍵iで開けることができる宝箱の番号jを0-indexedとして
# 1 << c_ij の総和を取ることで(たとえば宝箱0,1,3を開けられる鍵なら1011のように)表現できる
# よって、鍵を使うときの遷移は、現在の宝箱の開封情報と、鍵で開けられる宝箱の情報とでビット単位ORを取ればよい

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    c = list(map(int, sys.stdin.readline().split()))
    k = 0
    for x in c:
        k += 1 << (x-1)
    keys.append([k, a])

INF = 10**9
dp = [[INF]*(2**n) for _ in range(m+1)]
dp[0][0] = 0

for i in range(m):
    ki, ai = keys[i]

    for j in range(2**n):

        if dp[i][j] < INF:

            j_next = j | ki
            dp[i+1][j_next] = min(dp[i+1][j_next], dp[i][j]+ai)

            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

ans = INF
for i in range(1, m+1):
    tmp = dp[i][-1]
    ans = min(ans, tmp)

if ans < INF:
    print(ans)
else:
    print(-1)