N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(set(map(int, input().split())))

B = sorted(B)
M = len(B)
ans = 10**9
import bisect

for a in A:
    idx_r = bisect.bisect_right(B, a)

    if idx_r > 0 and idx_r < M:
        tmp = min([ abs(B[idx_r-1]-a) , abs(B[idx_r]-a) ])
    elif idx_r == 0:
        tmp = abs(B[0]-a)
    elif idx_r == M:
        tmp = abs(B[M-1]-a)

    if tmp < ans:
        ans = tmp

print(ans)