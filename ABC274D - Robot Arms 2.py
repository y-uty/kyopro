N, x, y = map(int, input().split())
A = list(map(int, input().split()))

# x, y座標それぞれで部分和DPする
x_dp = [[False]*(2*(10**4)+1) for _ in range(N+1)] # -10000 ~ 0 ~ 10000
y_dp = [[False]*(2*(10**4)+1) for _ in range(N+1)]

# すべての座標を+10000して扱う
offset = 10**4

x_dp[0][0+offset] = True
x_dp[1][A[0]+offset] = True
for i in range(1, N):
    for j in range(2*(10**4)+1):
        if x_dp[i][j]:
            if i%2==1:
                x_dp[i+1][j] = x_dp[i][j]

            else:
                x_dp[i+1][j+A[i]] = True
                x_dp[i+1][j-A[i]] = True

y_dp[0][0+offset] = True
for i in range(N):
    for j in range(2*(10**4)+1):
        if y_dp[i][j]:
            if i%2==0:
                y_dp[i+1][j] = y_dp[i][j]
            else:
                y_dp[i+1][j+A[i]] = True
                y_dp[i+1][j-A[i]] = True

# print(x_dp[N][x+offset])
# print(y_dp[N][y+offset])

if x_dp[N][x+offset] and y_dp[N][y+offset]:
    print('Yes')
else:
    print('No')
