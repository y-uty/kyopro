K = int(input())
Cities = [ tuple(map(int, input().split())) for _ in range(K)]

# 2点間距離の前計算
Dist_list = [[0]*K for _ in range(K)]
for i in range(K):
    for j in range(K):
        Xfrom, Yfrom = Cities[i]
        Xto, Yto = Cities[j]
        Dist_list[i][j] = ((Xto-Xfrom)**2 + (Yto-Yfrom)**2)**0.5     

# bitDPによるTSPの計算量 O(N^2 2^N)
# dp[i][j]:= 訪問済み頂点集合iで、現在位置がjのときの移動距離のMin
INF = 10**15
dp = [[INF]*K for _ in range(2**K)]
dp[0][0] = 0

for i in range(1<<K): # 集合iが訪問済みで、
    # (終点である始点が訪問済み -> それ以上移動する必要がないのでSkip)
    if i%2: continue

    for j in range(K): # 現在地jの状態から、
        # (jが未訪問 -> iにjが含まれていないことになり、その経路はありえないのでSkip)
        if dp[i][j] < INF:

            for k in range(K): # 次の訪問先kへ移動する.
                # (kが訪問済み -> iに含まれる地点をもう一度訪れる必要がないのでSkip)
                if (i//(1<<k))%2 == 0:

                    # 遷移
                    dp[i | (1<<k)][k] = min(dp[i | (1<<k)][k], dp[i][j]+Dist_list[j][k])

print(dp[(1<<K)-1][0])