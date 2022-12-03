import collections
n, m = map(int, input().split())

# M=a^2+b^2 となるような非負整数a,b(a<=b)の組を見つける
ab = []
for i in range(1001):
    for j in range(i, 1001):
        if i**2+j**2==m:
            ab.append((i, j))

# (a, b)の組を元に、1手で移動できる先を列挙する
vx, vy = [], []
for i in range(len(ab)):
    a, b = ab[i]
    ex = [a, b, -a, -b,  a, -a, b, -b]
    ey = [b, a, -b, -a, -b,  b,-a,  a]
    for i in range(8):
        vx.append(ex[i])
        vy.append(ey[i])

# グリッド上をBFS
masu = [[-1]*n for _ in range(n)]
nx = collections.deque()
nx.append((0, 0))
masu[0][0] = 0

while nx:
    x_from, y_from = nx.popleft()

    for i in range(len(vx)):
        x_to = x_from + vx[i]
        y_to = y_from + vy[i]

        if x_to >= 0 and x_to < n and y_to >= 0 and y_to < n:
            if masu[x_to][y_to] < 0:
                masu[x_to][y_to] = masu[x_from][y_from] + 1
                nx.append((x_to, y_to))

for i in range(n):
    print(*masu[i])