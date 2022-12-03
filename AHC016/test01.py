def main():

    ## 入力 ##
    M, ErrorRate = input().split() # 出力グラフ数, エラー率(0.00~0.40)
    M, ErrorRate = int(M), float(ErrorRate)

    ## 変数 ##
    if ErrorRate >= 0.15:
      EdgeNumUnit = 49
    elif ErrorRate >= 0.10:
      EdgeNumUnit = 15
    elif ErrorRate > 0.0:
      EdgeNumUnit = 10
    else:
      EdgeNumUnit = 1
    EdgeNumAtLeast = M*EdgeNumUnit # 出力グラフ数 * 出力グラフごとに辺の本数を何本ずつ増やすか
    N = GetEdgeMaxNum(EdgeNumAtLeast) 

    EdgeMaxNum = N*(N-1)//2 # 出力するグラフの最大の辺の数(=出力するグラフの01文字列の長さ)
    G = [] # M個のグラフを格納する配列
    EdgeNumList = [] # グラフごとの辺の数を格納する配列
    EdgeExpectList = [] # エラー率から期待される、受け取るグラフHの辺の本数を格納する配列

    ## 出力作成処理 ##
    # 方針： M個のグラフに張る辺の数で各グラフを区別する
    for GraphId in range(1, M+1):
        g = []
        for j in range(EdgeMaxNum):
            EdgeNum = EdgeNumUnit * GraphId
            if j < EdgeNum:
                g.append('1')
            else:
                g.append('0')
            
        EdgeNumList.append(EdgeNum)
        EdgeExpect = EdgeNum*(1-ErrorRate) + (EdgeMaxNum-EdgeNum)*ErrorRate
        EdgeExpectList.append(EdgeExpect)
        G.append(''.join(g))

    # print(EdgeExpectList)
    # sys.stdout = open('./out01.txt', 'w')
    # # sys.stdin = open('./in01.txt', 'r')

    ## 出力 ##
    # 作成したグラフを出力する
    print(N)
    sys.stdout.flush()
    for i in range(M):
        print(G[i])
        sys.stdout.flush()
    
    ## クエリ処理 ##
    for _ in range(100):
        h = input() # グラフを受け取り、辺の本数を数える
        EdgeCountOfH = collections.Counter(h)['1']

        # 予め求めた、グラフgごとのhの辺の本数の期待値のうち、
        # 実際のhの辺の本数との差の絶対値が最も小さいものを予測値とする
        MinAbsDiff, PredictedId = 10000.0, -1
        for i in range(M):
            AbsDiff = abs(EdgeExpectList[i] - EdgeCountOfH)
            if AbsDiff < MinAbsDiff:
                MinAbsDiff = AbsDiff
                PredictedId = i

        # 予測値を出力
        print(PredictedId)
        sys.stdout.flush()       


def GetEdgeMaxNum(EdgeNumAtLeast):
    EdgeMaxNumbers = [0,
                        0, 1, 3, 6, 10, 15, 21, 28, 36, 45,
                        55, 66, 78, 91, 105, 120, 136, 153, 171, 190,
                        210, 231, 253, 276, 300, 325, 351, 378, 406, 435,
                        465, 496, 528, 561, 595, 630, 666, 703, 741, 780,
                        820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225,
                        1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770,
                        1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415,
                        2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160,
                        3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005,
                        4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950,
                    10000]
    idx_r = bisect.bisect_left(EdgeMaxNumbers, EdgeNumAtLeast)
    return idx_r


if __name__=='__main__':
    import sys
    import collections
    import bisect

    main()