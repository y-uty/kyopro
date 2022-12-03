h, w = map(int, input().split())
r, c = map(int, input().split())
ans = 0

for i in range(1, h+1):
    for j in range(1, w+1):
        if i==r and j==c:
            continue
        else:
            if abs(i-r)+abs(j-c)==1:
                ans += 1

print(ans)