N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

aok = 1
bok = 1

for i in range(N-1):

    if aok == 1:
        diffa = 1
    else:
        diffa = 0
    
    if bok == 1:
        diffb = 1
    else:
        diffb = 0

    if (abs(A[i+1] - A[i]) <= K and diffa == 1) or (abs(A[i+1] - B[i]) <= K and diffb == 1):
        aok = 1
    else:
        aok = 0

    if (abs(B[i+1] - A[i]) <= K and diffa == 1) or (abs(B[i+1] - B[i]) <= K and diffb == 1):
        bok = 1
    else:
        bok = 0
 
    if aok + bok == 0:
        print('No')
        exit()

print('Yes')