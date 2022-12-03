def main():
    N, M = map(int, sys.stdin.readline().split())

    # 原点に戻ってくるまでに、宝箱は訪れても訪れなくても良い
    # 宝箱を含めた全点でTSPをして、宝箱以外全訪問済みの集合で、宝箱の訪問有無(2^M)を全探索する
    Cities = [(0, 0)]
    for _ in range(N+M):
        Cities.append(tuple(map(int, sys.stdin.readline().split())))

    K = N+M+1 # 全訪問先の数(K<=18)
    INF = 10**12
    # ブースターの使用個数を数えるためのビットマスクを作成
    Booster_Mask = 0
    for i in range(K-1, N, -1): Booster_Mask += 1<<i

    # 2点間距離の前計算
    Dist_list = [[0]*K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            Xfrom, Yfrom = Cities[i]
            Xto, Yto = Cities[j]
            Dist_list[i][j] = ((Xto-Xfrom)**2 + (Yto-Yfrom)**2)**0.5     

    # bitDPによるTSPの計算量 O(N^2 2^N)
    # dp[i][j]:= 訪問済み頂点集合iで、現在位置がjのときの移動距離のMin
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
                        # ブースターの使用個数
                        Boosted = 1 << popcount(i&Booster_Mask)

                        # 遷移
                        dp[i | (1<<k)][k] = min(dp[i | (1<<k)][k], dp[i][j]+Dist_list[j][k]/Boosted)

    ans = INF
    # 必要な地点をすべて訪問して始点に戻ってきた経路で、
    # 各ブースターを使った/使ってないの2^M通りのうち最小のものが答え
    for i in range(1<<M):
        tmp = dp[(i << (N+1)) + (1<<(N+1))-1][0]
        if tmp < ans:
            ans = tmp

    print(ans)


def popcount(n: int) -> int:
    # assert -(1 << 63) <= n < 1 << 63
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c

if __name__=='__main__':
    import sys
    main()
