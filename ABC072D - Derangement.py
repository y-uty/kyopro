n = int(input())
p = list(map(int, input().split()))

ans = []
pair = False
for i in range(n):
    if i+1 == p[i]:
        if pair:
            pair = False
        else:
            ans.append(i)
            pair = True
    else:
        pair = False

print(len(ans))