n, m = map(int, input().split())
if m==0:
    print(1)
    exit()

a = [0] + sorted(list(map(int, input().split()))) + [n+1]

x = []
for i in range(m+1):
    wh = a[i+1]-a[i]-1
    if wh > 0:
        x.append(a[i+1]-a[i]-1)

if len(x)==0:
    print(0)
    exit()

k = min(x)
ans = 0
for y in x:
    ans += (y+k-1) // k

print(ans)