N, M = map(int, input().split())
pica = []
picb = []
for i in range(N):
    pica += list(str(input()))
for i in range(M):
    picb += list(str(input()))

ans = 0
for i in range(N-M+1):
    for j in range(N-M+1):
        matched = True
        for k in range(M):
            for l in range(M):
                matched &= True if pica[N*(i+k)+j+l] == picb[M*k+l] else False

        if matched:
            print('Yes')
            exit()

print('No')