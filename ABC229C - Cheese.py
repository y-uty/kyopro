N, W = map(int, input().split())
cheese = []
for i in range(N):
    a, b = map(int, input().split())
    cheese.append([a, b])

cheese.sort(reverse=True)
deli = 0

for i in range(N):
    if cheese[i][1] <= W:
        deli += cheese[i][0] * cheese[i][1]
        W -= cheese[i][1]
    else:
        deli += cheese[i][0] * W
        print(deli)
        exit()

print(deli)
