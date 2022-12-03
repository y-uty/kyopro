w, h, n = map(int, input().split())

x_seg = [0, w]
y_seg = [0, h]

for _ in range(n):
    x, y, a = map(int, input().split())

    if a==1:
        x_seg[0] = max([x_seg[0], x])
    elif a==2:
        x_seg[1] = min([x_seg[1], x])
    elif a==3:
        y_seg[0] = max([y_seg[0], y])
    else:
        y_seg[1] = min([y_seg[1], y])

x = max([(x_seg[1]-x_seg[0]), 0])
y = max([(y_seg[1]-y_seg[0]), 0])
print(x*y)