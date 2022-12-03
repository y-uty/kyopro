import sys
h, w, d = map(int, input().split())

# 1~HWの整数が描かれた座標を調べる(配列に記録していく)
# 1->1+D->1+2D, ... の順に、座標のマンハッタン距離でコストを計算していく
# L<=Rより、スタート地点より小さい整数が書かれたマスに移動することは無いので
# 1~D-1までを起点としてコストを調べればよく、それはO(HW)ですむ

# 整数iがどの座標にいるかをnum[i]に記録
num = [0]*(h*w+1)
for i in range(h):
    a_row = list(map(int, sys.stdin.readline().split()))
    for j in range(w):
        num[a_row[j]] = (i+1, j+1)

# 1<=i<Dなるすべてのiについて、コストをi起点(0)としてi+D,i+2D,...と計算していく
cost = [0]*(h*w+1)
for i in range(1, 1+d):
    j = i+d
    while j <= h*w:
        cost[j] = abs(num[j-d][0]-num[j][0])+abs(num[j-d][1]-num[j][1])+cost[j-d]
        j += d

# 各クエリについて、計算済みのコストの差が答え
q = int(input())
for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    print(cost[r]-cost[l])
