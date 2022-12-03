import collections
H, W = map(int, input().split())
masu = []
v_start = (-1, -1, -1)
for i in range(H):
    x = input()
    masu_r = []
    for j in range(W):
        if x[j]=='S':
            v_start = (i, j, -1)
        masu_r.append(x[j])
    masu.append(masu_r)


# 4近傍gridDFS
# 来た方向を除く3方向に進み、進んだ先が始点と一致したらOK
# 一致せずに終わったらNG
vr = [0, 1, 0, -1]
vc = [1, 0, -1, 0]

seen = [[False]*W for _ in range(H)]
nx = collections.deque()
nx.append(v_start)

while nx:
    from_r, from_c, from_dir = nx.pop()
    seen[from_r][from_c] = True

    for i in range(4):

        # 元には戻らない
        if from_dir >= 0 and from_dir==(i+2)%4:
            continue
        to_r = from_r + vr[i]
        to_c = from_c + vc[i]

        if to_r >= 0 and to_r < H and to_c >= 0 and to_c < W:
            if masu[to_r][to_c]=='#':
                continue
            elif masu[to_r][to_c]=='S':
                print('Yes')
                exit()
            else:
                if not seen[to_r][to_c]:
                    nx.append((to_r, to_c, i))

print('No')