import sys
n, q = map(int, input().split())
a = list(map(int, input().split()))

# swapはO(1)で可能
# shiftはそれ自体はキューを使うことでO(1)で可能だが、
# t=3のクエリでprintするときのランダムアクセスがO(N)になってしまう

# そこで、データ構造は通常の配列のままとして、
# 現在の先頭を指すインデックスをオフセットとして計算することで解決する

# 右にshiftする場合、その前の時点の末尾の要素が先頭にくる
# 従って、オフセットにN-1を加算する
# 2回目以降は、オフセットを加算したあとにNで割った余りとすればよい
# 先頭要素の位置さえわかれば、swapする要素のインデックスが与えられても同様に対応できる

offset = 0
for _ in range(q):
    t, x, y = map(int, sys.stdin.readline().split())

    # x, yに対する現在の配列のインデックスを先に求める
    # インデックスが与えられない場合(=0)も使わないだけなので気にしなくてOK
    idx_x = (x-1 + offset)%n
    idx_y = (y-1 + offset)%n
    
    # t=1: swap
    if t==1:
        a[idx_x], a[idx_y] = a[idx_y], a[idx_x]
    
    # t=2: shift right (rotate)
    elif t==2:
        offset += n-1
        offset %= n

    # t=3: print
    else:
        print(a[idx_x])
