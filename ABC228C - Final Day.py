N, K = map(int, input().split())
import bisect
s = []

for i in range(N):
    d1, d2, d3 = map(int, input().split())
    s.append(d1+d2+d3)

sorted_s = sorted(s)
for i in range(N):
    cnt = N - bisect.bisect_right(sorted_s, s[i]+300)
    if cnt + 1 <= K:
        print('Yes')
    else:
        print('No')