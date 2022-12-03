import sys
n = int(input())
x, y = map(int, input().split())

INF = 301 # 制約N<=300より.
dp = [[INF]*(y+1) for _ in range(x+1)]
lbox = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lbox.append((a, b))

#dp[k][i][j]:=k番目までの弁当からx=i,y=jとなるように選ぶ弁当個数の最小値.
for k in range(n):
    la, lb = lbox[k]

    # 3次元配列は重いので、dp[k][.][.]の部分はdp[.][i][j]を使い回す.
    # i, jは単調増加に遷移するので、状態は大きい方から見ていく.
    # (そうしないと、遷移先の状態をまた遷移させてしまう)
    for i in range(x, 0, -1):
        for j in range(y, 0, -1):
            if dp[i][j] < INF:
                # i, jが X, Y以上になればよいので、X, Yを超えたら丸める.
                # これにより状態数をX*Yにおさえられる(全体でO(NXY)となり間に合う).
                ix = x if i+la > x else i+la
                jy = y if j+lb > y else j+lb
                dp[ix][jy] = min([dp[ix][jy], dp[i][j]+1])

    # 単独選択は最後に更新(大きい方から見ていったので).
    # i=a,j=bに関しては必ず最適な選び方(1個)となる. ただし単独でX, Yを超えるケースに注意.
    la = x if la > x else la
    lb = y if lb > y else lb
    dp[la][lb] = 1

# 状態を丸めたので答えはi=X,j=Yにいる.
# 一度も更新されていない場合、達成不可能.
if dp[x][y]==INF:
    print(-1)
else:
    print(dp[x][y])
