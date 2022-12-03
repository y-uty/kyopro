n, k = map(int, input().split())
a = list(map(int, input().split()))
R = [0]*n # 右端のスタート地点

ans = 0
for l in range(n-1):

    # 右端のスタート地点を決める
    if l==0:
        R[0] = 0
    else:
        R[l] = R[l-1]

    # 右端を1つずらして、条件を満たすならまだ繰り返す
    while (R[l] < n-1) and (a[R[l]+1]-a[l] <= k):
        R[l] += 1 

    # 答えは、各左端lに対する最大の右端rとしたとき、r-l
    ans += R[l] - l 

print(ans)