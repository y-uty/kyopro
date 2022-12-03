import sys
import bisect
N, p, q = map(int, input().split())
score_std = [0]
score_bisect = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())

    S = p*a+q*b
    score_std.append(S)
    score_bisect.append(S)

score_bisect = sorted(list(score_bisect))

ans = [0]*(N+1)
for i in range(1, N+1):
    Si = score_std[i]

    rank = N - bisect.bisect_right(score_bisect, Si) + 1

    ans[i] = rank

# print(score_std)
# print(score_bisect)

print(*ans[1:], sep='\n')