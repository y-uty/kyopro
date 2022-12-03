import sys
n, w = map(int, input().split())

plans = [0]*(n+1)
csum = 0

for _ in range(n):
    s, t, p = map(int, sys.stdin.readline().split())
    plans[s] += p
    plans[t] -= p

for x in plans:
    csum += plans[x]
    if csum > w:
        print('No')
        exit()

print('Yes')