N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if A[i] == B[i]:
        cnt += 1

print(cnt)

seta = set(A)
setb = set(B)

print(len(seta & setb)-cnt)