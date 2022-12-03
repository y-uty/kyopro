import sys
n, q = map(int, input().split())

a = list(range(0, n+1))
p = list(range(0, n+1))

for _ in range(q):
    x = int(sys.stdin.readline())

    # ボールxは何番目にある？
    x_pos = p[x]

    # ボールxの右隣(=x_pos+1番目)はどのボール？
    ## xが右端の場合だけ左隣
    x_pos_next = x_pos + 1 if x_pos < n else x_pos - 1
    ball_next = a[x_pos_next]

    # 「何番目か」を入れ替え
    p[x], p[ball_next] = p[ball_next], p[x]

    # ボールの入れ替え
    a[x_pos], a[x_pos_next] = a[x_pos_next], a[x_pos]

print(*a[1:])