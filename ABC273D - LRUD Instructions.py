import sys
import collections
import bisect
h, w, rs, cs = map(int, input().split())
wall_r = collections.defaultdict(list) # r行目に壁がある列番号
wall_c = collections.defaultdict(list) # c行目に壁がある行番号

n = int(input())
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())

    wall_r[r].append(c)
    wall_c[c].append(r)

for k, v in wall_r.items():
    wall_r[k].append(0)
    wall_r[k].append(w+1)
    wall_r[k].sort()

for k, v in wall_c.items():
    wall_c[k].append(0)
    wall_c[k].append(h+1)
    wall_c[k].sort()


q = int(input())
now_r, now_c = rs, cs
for _ in range(q):
    d, l = map(str, sys.stdin.readline().split())
    l = int(l)

    if d=='L':
        next_r = now_r
        next_c = max(now_c - l, 1) # はみ出し注意

        # その行に全く壁がなければ、l歩先へ移動する
        if len(wall_r[now_r])==0:
            now_r = next_r
            now_c = next_c
        # 壁がある場合、l歩先か、直近の壁の1つ前か、のより近い方に移動する
        else:
            idx_wall = bisect.bisect_right(wall_r[now_r], now_c)
            now_c = max(wall_r[now_r][idx_wall-1]+1, next_c)

    elif d=='R': # Lと逆方向
        next_r = now_r
        next_c = min(now_c + l, w) # はみ出し注意

        # その行に全く壁がなければ、l歩先へ移動する
        if len(wall_r[now_r])==0:
            now_r = next_r
            now_c = next_c
        # 壁がある場合、l歩先か、直近の壁の1つ前か、のより近い方に移動する
        else:
            idx_wall = bisect.bisect_right(wall_r[now_r], now_c)
            now_c = min(wall_r[now_r][idx_wall]-1, next_c)

    elif d=='U':
        next_r = max(now_r - l, 1) # はみ出し注意
        next_c = now_c

        # その行に全く壁がなければ、l歩先へ移動する
        if len(wall_c[now_c])==0:
            now_r = next_r
            now_c = next_c
        # 壁がある場合、l歩先か、直近の壁の1つ前か、のより近い方に移動する
        else:
            idx_wall = bisect.bisect_right(wall_c[now_c], now_r)
            now_r = max(wall_c[now_c][idx_wall-1]+1, next_r)       

    else:
        next_r = min(now_r + l, h) # はみ出し注意
        next_c = now_c

        # その行に全く壁がなければ、l歩先へ移動する
        if len(wall_c[now_c])==0:
            now_r = next_r
            now_c = next_c
        # 壁がある場合、l歩先か、直近の壁の1つ前か、のより近い方に移動する
        else:
            idx_wall = bisect.bisect_right(wall_c[now_c], now_r)
            now_r = min(wall_c[now_c][idx_wall]-1, next_r)


    print(now_r, now_c)