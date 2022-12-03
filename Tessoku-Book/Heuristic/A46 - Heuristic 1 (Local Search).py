# 必要ライブラリのimport
import sys
import random

# 入力
N = int(input())
Cities = [ tuple(map(int, sys.stdin.readline().split())) for _ in range(N) ]


# 都市間距離の前計算
Distance = [ [0]*N for _ in range(N) ]
for i in range(N-1):
    for j in range(i+1, N):
        d = ( (Cities[i][0]-Cities[j][0])**2 + (Cities[i][1]-Cities[j][1])**2 )**0.5
        Distance[i][j] = d
        Distance[j][i] = d


# 局所探索法
# 小さな変更(近傍)をランダムに行い、スコアが改善すればそれを採択し、そうでなければ棄却する

# 初期状態の生成：貪欲法で求める
Path_list = [0]
Visited = [False]*N
Visited[0] = True
C_from = 0
Score_now = 0
for _ in range(N-1):
    Best_dist = 10**9
    Best_C_to = -1
    
    for C_to in range(N):

        if not Visited[C_to]:
            This_dist = Distance[C_from][C_to]
            if This_dist < Best_dist:
                Best_dist = This_dist
                Best_C_to = C_to

    Visited[Best_C_to] = True
    C_from = Best_C_to
    Path_list.append(Best_C_to)
    Score_now += Best_dist

Score_now += Distance[Path_list[-1]][0]
Path_list.append(0)

# 指定回数繰り返す
Repeat_num = 5*10**5

for n in range(Repeat_num):
    # 近傍: 1,...,1のN+1項の数列のL(>=2)番目からR(<=N)番目までを反転させる
    L = random.randint(1, N-1)
    R = random.randint(1, N-1)
    if L > R: L, R = R, L # L < R に.

    # L ~ R を反転させたあと、L-1 ~ R+1 までのスコアの変化を計算する(それ以外は変化しない)

    # [L, R]が関与する部分だけのスコアを求めるfunction
    def calc_score_range(l, r):
        sc = 0
        for i in range(l-1, r+1): sc += Distance[Path_list[i]][Path_list[i+1]]
        return sc

    # 区間反転と前後のスコア計算
    Score_Bef = calc_score_range(L, R)
    for i in range(L, (L+R+1)//2):
        Path_list[i], Path_list[L+R-i] = Path_list[L+R-i], Path_list[i]
    Score_Aft = calc_score_range(L, R)

    # スコアが改善された場合は採用、そうでなければもとに戻す
    if Score_Aft < Score_Bef:
        Score_now -= (Score_Bef - Score_Aft)
    else:
        for i in range(L, (L+R+1)//2):
            Path_list[i], Path_list[L+R-i] = Path_list[L+R-i], Path_list[i]

    # if n%1000==0: print(n+1, Score_now)

# 出力
for ans in Path_list:
    print(ans+1)
