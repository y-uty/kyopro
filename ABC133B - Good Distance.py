N, D = map(int, input().split())
X = []
cnt = 0

for i in range(N):
    X.append(list(map(int, input().split())))

for j in range(N):
    for l in range(j+1, N):
        d = 0
        for k in range(D):
            d += (X[j][k] - X[l][k])**2
        d = d**0.5
        if d.is_integer():
            cnt += 1

print(cnt)