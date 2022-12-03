import sys
import collections
h, w, n = map(int, input().split())

# 中心を(i, j)とする3x3のマスが何マス塗られているか
masu3x3 = collections.defaultdict(int)

# 8近傍+中心
vx = [-1, 0, 1, -1, 1, -1, 0, 1, 0]
vy = [1, 1, 1, 0, 0, -1, -1, -1, 0]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    # (a, b)が塗られると、それが3x3マスのいずれかに位置する、
    # (最大で)異なる9つの3x3マスの塗りマスが1つずつ増える
    for i in range(len(vx)):
        dx, dy = vx[i], vy[i]
        x, y = a+dx, b+dy

        # 3x3マスの中心になるためには、縦も横も両端マスでないこと
        if x > 1 and x < h and y > 1 and y < w:
            masu3x3[(x, y)] += 1

ans = [0]*10
tot = 0
for v in masu3x3.values():
    ans[v] += 1
    tot += 1

ans[0] = (h-2)*(w-2) - tot

print(*ans, sep='\n')