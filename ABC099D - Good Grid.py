# (x+y)%3 =0, 1, 2のすべてのマスについて、色1~30で塗ったときのコスト総和を先に求める
# cost[i][m]:= (x+y)%3=mのマスをiに塗り替えたコストの総和
# 1~30から30P3で色番号をとってa, b, cとして、min(cost[0][a]+cost[1][b]+cost[2][c])を調べる

N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
color = [list(map(int, input().split())) for _ in range(N)]

cost = [[0]*C for _ in range(3)]
for x in range(N):
    for y in range(N):
        r = x+1
        c = y+1
        m = (r+c)%3
        for i in range(C):
            cost[m][i] += D[color[x][y]-1][i]

num = list(range(C))
import itertools
painted = itertools.permutations(num, 3)
ans = 10**15
for p in painted:
    c1, c2, c3 = p
    ans = min(ans, cost[0][c1]+cost[1][c2]+cost[2][c3])

print(ans)