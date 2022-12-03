H, W = map(int, input().split())

ans = [0]*W
for _ in range(H):
    C = list(input())
    for j in range(W):
        if C[j]=='#':
            ans[j] += 1

print(*ans)