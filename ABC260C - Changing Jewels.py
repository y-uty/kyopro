import collections
n, x, y = map(int, input().split())
r = 'red'
b = 'blue'

jewels = collections.deque()
jewels.append([n, r, 1])
bcnt = 0

while jewels:
    lv, col, num = jewels.popleft()
    if col==r: # 赤
        if lv > 1: # Lv1の赤い宝石はそれ以上何にも変換できない
            conv1 = [lv-1, r, num*1]
            conv2 = [lv, b, num*x]
            jewels.append(conv1)
            jewels.append(conv2)
    
    else: # 青
        if lv==1: # Lv1の青い宝石は答えに加算
            bcnt += num
        else:
            conv1 = [lv-1, r, num*1]
            conv2 = [lv-1, b, num*y]
            jewels.append(conv1)
            jewels.append(conv2)

print(bcnt)