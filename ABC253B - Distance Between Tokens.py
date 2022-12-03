h,w = map(int, input().split())
s = []
for _ in range(h):
    x = str(input())
    s.append(list(x))

x = []
for i in range(h):
    for j in range(w):
        if s[i][j]=='o':
            x.append([i, j])

print(abs(x[0][0]-x[1][0])+abs(x[0][1]-x[1][1]))