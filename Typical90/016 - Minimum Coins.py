n = int(input())
c = sorted(list(map(int, input().split())), reverse=True)

coinmax = c[0]
coinmed = c[1]
coinmin = c[2]

# N円を払うのに対して、2種類の硬貨の使用枚数がわかれば、
# 残り1種類は自ずと決まるため、これを探索する必要はない
# 制約が合計9999枚以下なので、全体で10000^2未満の探索で済む

ans = 10000
ulim = min([9999, n//coinmax])
for i in range(ulim, -1, -1):
    x = n - coinmax*i

    ulim2 = min([9999, x//coinmed])
    for j in range(ulim2, -1, -1):
        y = x - coinmed*j

        if y%coinmin==0:
            k = y//coinmin
            tmp = i+j+k
            if tmp < ans: ans = tmp

print(ans)