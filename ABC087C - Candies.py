N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ans = 0

for i in range(N):
    tmp = sum(A1[:i+1]) + sum(A2[i:])
    if tmp > ans: ans = tmp

print(ans)