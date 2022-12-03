n, k = map(int, input().split())
anumidx = []
anslist = [0] * n
A = list(map(int, input().split()))
for i in range(n):
    anumidx.append([A[i], i])

anumidx.sort()

faird, kdash = divmod(k, n)

for i in range(kdash):
    anslist[anumidx[i][1]] += 1

for ans in anslist:
    print(ans + faird)