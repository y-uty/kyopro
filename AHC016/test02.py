def main():

    ## 入力 ##
    # sys.stdin = open('./in01.txt', 'r')
    M, ErrorRate = input().split() # 出力グラフ数, エラー率(0.00~0.40)
    M, ErrorRate = int(M), float(ErrorRate)

    ## エラー率が0.00の場合、N=15で確実に予測できるため別処理 ##
    if ErrorRate==0.0:
      WhenErrDateIs0(M)
      exit()

    ## 変数 ##
    # 頂点数は100で固定
    N = 100
    EdgeMaxNum = N*(N-1)//2
    G = [] # G[i]:=i番目のグラフを表す01文字列


    ## 出力グラフGの作成 ##
    # 各Gk (1<=k<=M<=100)について、
    # k=1~60: 次数がN-1(全頂点と隣接)の頂点がk個あるグラフ
    # k=61~100: 次数が40の頂点がk-60個あるグラフ
    # 受け取ったグラフHについて、
    # 次数が60以上の頂点がs(>0)個あるとき、予測値をs-1(元のグラフがGs-1)、
    # 次数が60以上の頂点が0個で、次数が40以上の頂点がs(>0)個あるとき、予測値をs-1+60
    # とする
    for i in range(1, 101): # ひとまず100個つくってM個目までを採用することにする
        g = []
        if i <= 60: # 次数がN-1(全頂点と隣接)の頂点がk個あるグラフ
            for u in range(1, N):
                for v in range(u+1, N+1):
                    # 頂点u, v (u<v) 間の辺
                    if u <= i:
                        str01 = '1'
                    else:
                        str01 = '0'
                    g.append(str01)

        else: # 次数が40の頂点がk-60個あるグラフ
            for u in range(1, N):
                for v in range(u+1, N+1):
                    if u+60 <= i and v-u <= 40:
                        str01 = '1'
                    else:
                        str01 = '0'
                    g.append(str01)

        G.append(''.join(g))


    ## グラフGの出力 ##
    # sys.stdout = open('./out01.txt', 'w')
    print(N)
    sys.stdout.flush()
    for i in range(M):
        print(G[i])
        sys.stdout.flush()


    ## クエリ処理 ##
    for _ in range(100):
        h = input() # グラフを受け取る

        # 頂点ごとの次数をカウント
        DegreesIn = collections.defaultdict(int)
        Index_h = 0
        for i in range(1, N):
            for j in range(i+1, N+1):
                h01 = h[Index_h]
                if h01=='1':
                    DegreesIn[i] += 1
                    DegreesIn[j] += 1
                Index_h += 1
        # H -> G を決定
        In80GTE, In20GTE, Others = 0, 0, 0
        for k, v in DegreesIn.items():
            if v >= 60:
                In80GTE += 1
            elif v >= 20:
                In20GTE += 1
            else:
                Others += 1

        if In80GTE > 0:
            Predicted = min(In80GTE, 60, M) - 1
        elif In20GTE > 0:
            Predicted = min(In20GTE+60, M) - 1
        else:
            Predicted = random.randint(1, M) - 1
        
        # 出力
        print(Predicted)
        sys.stdout.flush()


def WhenErrDateIs0(M):
  N = 15
  G = []
  for i in range(M):
    g = []
    for j in range(N*(N-1)//2):
      if j < i:
        str01 = '1'
      else:
        str01 = '0'
      g.append(str01)
    G.append(''.join(g))
  
  print(N)
  for i in range(M):
    print(G[i])
  
  for _ in range(100):
    h = input()
    cnt1 = collections.Counter(h)['1']
    print(cnt1)

  return 0


if __name__=='__main__':
    import sys
    import random
    import collections

    main()
