N, K, X = map(int, input().split())
A = list(map(int, input().split()))

disc = []

for i in range(N):
    if K > 0:
        d, m = divmod(A[i], X)
        if d > K:
            disc.append(A[i] - X*K)
            K = 0
        else:
            disc.append(m)
            K -= d

    else:
        disc.append(A[i])
        
if K == 0:
    print(sum(disc))
else:
    disc.sort(reverse=True)
    for i in range(N):
        disc[i] = 0
        K -= 1
        if K == 0:
            break
    
    print(sum(disc))