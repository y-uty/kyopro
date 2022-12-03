H, W = list(map(int, input().split()))
A = []
for h in range(H):
    A.append(list(map(str, input().split())))

A_t = [list(a) for a in zip(*A)]

for w in range(W):
    print(' '.join(A_t[w]))