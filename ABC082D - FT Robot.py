s = input()
n = len(s)
s += 'T'
x, y = map(int, input().split())

turn_count = 0
forward_count = 0
X = []
Y = []
for i in range(n+1):
    if s[i]=='T':
        if turn_count%2==0:
            X.append(forward_count)
        else:
            Y.append(forward_count)
        forward_count = 0
        turn_count += 1

    else:
        forward_count += 1

# X, Yの総和より|x|, |y|が大きいとき、絶対に到達不可能
if abs(x) > sum(X) or abs(y) > sum(Y):
    print('No')
    exit()

offset_x = sum(X)
dp_x = [[False]*(2*offset_x+1) for _ in range(len(X)+1)]
dp_x[0][0+offset_x] = True

for i in range(len(X)):
    FX = X[i]
    for j in range(2*offset_x+1):

        if dp_x[i][j]:
            # x座標1回目の移動だけは+方向のみ
            dp_x[i+1][j+FX] = True
            if i > 0:
                dp_x[i+1][j-FX] = True

offset_y = sum(Y)
dp_y = [[False]*(2*offset_y+1) for _ in range(len(Y)+1)]
dp_y[0][0+offset_y] = True

for i in range(len(Y)):
    FY = Y[i]
    for j in range(2*offset_y+1):

        if dp_y[i][j]:
            dp_y[i+1][j+FY] = True
            dp_y[i+1][j-FY] = True

if dp_x[len(X)][x+offset_x] and dp_y[len(Y)][y+offset_y]:
    print('Yes')
else:
    print('No')
