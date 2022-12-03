import collections
n = int(input())
p = list(map(int, input().split()))

rel = collections.defaultdict(int)
for i in range(n-1):
    rel[i+2] = p[i]

ans = 0
ch = n
while ans<=n:
    pr = rel[ch]
    ans += 1
    if pr==1:
        print(ans)
        break
    ch = pr
