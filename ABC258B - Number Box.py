n = int(input())
a = []
for i in range(n):
    atmp = list(str(input()))
    a.append(atmp)

aex = []
for _ in range(3):
    for i in range(n):
        x = a[i]*3
        aex.append(x)

anslist = []
vx = [-1, 0, 1, -1, 1, -1, 0, 1]
vy = [1, 1, 1, 0, 0, -1, -1, -1]

for a in range(n):
    for b in range(n):

        for j in range(8):
            next_max = -1
            nx, ny = a+n, b+n
            tmp = aex[b+n][a+n]

            for i in range(n-1):
                nx, ny = nx+vx[j], ny+vy[j]
                tmp += aex[ny][nx]
               
            anslist.append(int(tmp))
            
print(max(anslist))