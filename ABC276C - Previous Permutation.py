import bisect
N = int(input())
P = list(map(int, input().split()))

x = P[-1]
for i in range(1, N):
    if P[-1-i] > x:
        y = P[-1-i] # はじめて単調減少でなくなった数
        pos = N-i-1
        break
    else:
        x = P[-1-i]

tmp = P[pos:]
tmp_sorted = sorted(tmp)

# yより小さい最大値をみつける
idx = bisect.bisect_left(tmp_sorted, y)-1
z = tmp_sorted[idx]

ans = P[:pos]
ans.append(z)
tmp.remove(z)
tmp.sort(reverse=True)
ans += tmp

print(*ans)
