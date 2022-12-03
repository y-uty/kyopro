import sys
import bisect
A, B, Q = map(int, input().split())
S = [-10**10]
T = [-10**10]
for _ in range(A):
    s = int(sys.stdin.readline())
    S.append(s)
S.append(2*(10**10))
for _ in range(B):
    t = int(sys.stdin.readline())
    T.append(t)
T.append(2*(10**10))

for _ in range(Q):
    x = int(sys.stdin.readline())

    idx_S = bisect.bisect_right(S, x)
    idx_T = bisect.bisect_right(T, x)

    near_S = [S[idx_S-1], S[idx_S]]
    near_T = [T[idx_T-1], T[idx_T]]

    anscand = []
    for i in range(2):
        for j in range(2):
            s, t = min(near_S[i], near_T[j]), max(near_S[i], near_T[j])

            if s <= x and x <= t:
                tmp = min(2*abs(x-s)+abs(x-t), 2*abs(x-t)+abs(x-s))
            elif t < x:
                tmp = abs(x-s)
            else:
                tmp = abs(t-x)

            anscand.append(tmp)

    print(min(anscand))
