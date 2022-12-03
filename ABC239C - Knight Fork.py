x1, y1, x2, y2= map(int, input().split())

cnt = 0

for x in range(x1-2, x1+3):
    for y in range(y1-2, y1+3):
        dist_x1 = abs(x - x1)
        dist_y1 = abs(y - y1)
        dist_x2 = abs(x - x2)
        dist_y2 = abs(y - y2)

        if dist_x1**2 + dist_y1**2 == 5:
            if dist_x2**2 + dist_y2**2 == 5:
                cnt += 1

if cnt == 0:
    print('No')
else:
    print('Yes')
