n, k = map(int, input().split())
ans = 10**9

ts = []
for i in range(n):
    ts.append(int(input()))

ts.sort()

for i in range(n-k+1):
    tmp = abs(ts[i] - ts[i+k-1])
    if tmp < ans:
        ans = tmp

print(ans)