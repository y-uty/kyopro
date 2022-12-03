N = int(input())
P = list(map(int, input().split()))
Q = [0] * N

for i in range(N):
    p = P[i]
    Q[p-1] = str(i+1)

print(' '.join(Q))