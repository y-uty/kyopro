N = int(input())
S = list(input())
Q = int(input())
mirror = 0

for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if mirror % 2 == 1:
            a += N if a <= N else -1 * N
            b += N if b <= N else -1 * N

        tmpa = S[a-1]
        tmpb = S[b-1]
        S[a-1] = tmpb
        S[b-1] = tmpa

    else:
        mirror += 1

if mirror % 2 == 0:
    print(''.join(S))
else:
    print(''.join(S[N:] + S[:N]))