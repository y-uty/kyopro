n, m = map(int, input().split())
attend = [[0]*n for _ in range(n)]

for _ in range(m):
    a = list(map(int, input().split()))
    k = a[0]
    x = a[1:]
    for i in range(k-1):
        for j in range(i+1, k):
            p1 = x[i]-1
            p2 = x[j]-1
            attend[p1][p2] += 1


for i in range(n-1):
    for j in range(i+1, n):
        if attend[i][j]==0:
            print('No')
            exit()

print('Yes')
