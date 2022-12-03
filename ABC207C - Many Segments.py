import sys
n = int(input())
ans = 0

segs = []
for _ in range(n):
    t, l, r = map(int, sys.stdin.readline().split())
    if t in (2, 4): r -= 0.1
    if t in (3, 4): l += 0.1
    segs.append([l, r])

for i in range(n):
    for j in range(i+1, n):
        if segs[i][1] < segs[j][0] or segs[j][1] < segs[i][0]:
            pass
        else:
            ans += 1

print(ans)