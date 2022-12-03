N = int(input())
T = str(input())

xy = [0,0]

dir = 0

for t in T:
    if t == 'R':
        dir += 1
    else:
        dir = dir % 4
        if dir == 0:
            xy[0] += 1
        elif dir == 1:
            xy[1] -= 1
        elif dir == 2:
            xy[0] -= 1
        else:
            xy[1] += 1

print(str(xy[0]) + ' ' + str(xy[1]))