import collections
N = int(input())
A = list(map(int, input().split()))
A.append(A[-1])
S = list(map(int, input().split()))

ans = 0
MOD = 998244353

Scsum = [0]
for i in range(N):
    Scsum.append((Scsum[-1]+S[i])%MOD)

numset = set()
j = 0
for i in range(N):

    while True:
        if A[j] not in numset:
            numset.add(A[j])
            j += 1
        else:
            ans += Scsum[j-i]
            ans %= MOD
            break

    numset.discard(A[i])

print(ans)