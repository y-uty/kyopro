x, y, z = map(int, input().split())

# x, yが逆側にある場合、xに向かえばよい
if x*y < 0:
    print(abs(x))
    exit()

# xがyより手前にある場合、xに向かえばよい
if abs(x) < abs(y):
    print(abs(x))
    exit()

# x, yが同じ側にあり、かつxが壁のむこうであるときだけを考える

# ハンマーが壁と逆側にある場合、取りに戻る
if z*y < 0:
    print(2*abs(z)+abs(x))

else:
    # 同じ側にある場合、拾えない場合はNG
    if abs(z) > abs(y):
        print(-1)
    else:
        # 拾えるなら、そのままxに向かうだけ
        print(abs(x))