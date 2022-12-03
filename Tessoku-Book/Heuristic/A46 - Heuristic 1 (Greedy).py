# 必要ライブラリのimport
import sys

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


# 次に向かう都市を貪欲に決める
Ans_out = [0]

Visited = [False]*N
Visited[0] = True
C_from = 0
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
    Ans_out.append(Best_C_to)  

Ans_out.append(0)

# 出力
Score = 0
for i in range(N+1):
    print(Ans_out[i]+1)
    if i < N:
        Score += Distance[Ans_out[i]][Ans_out[i+1]]

# print(Score)
