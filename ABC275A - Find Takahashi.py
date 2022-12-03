N = int(input())
ans = 0
tmp = -1
H = list(map(int, input().split()))
for i in range(N):
    if H[i] > tmp:
        ans = i+1
        tmp = H[i]

print(ans)