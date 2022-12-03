N = int(input())

A = list(map(int, input().split()))
ans = 0

cumsum = 0
sqrsum = 0
for i in range(N):
    cumsum += A[i]
    sqrsum += (A[i])**2

print(N * sqrsum - (cumsum)**2)