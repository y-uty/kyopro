n, m = map(int, input().split())

Xmodm = [[0]*9]
for i in range(n):
    tmp = []
    for j in range(9):
        tmp.append((Xmodm[i][j]*10+(j+1))%m)
    Xmodm.append(tmp)

for i in range(n, 0, -1):
    for j in range(8, -1, -1):
        if Xmodm[i][j]==0:
            print(str(j+1)*i)
            exit()

print(-1)
