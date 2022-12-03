import sys
n, q = map(int, input().split())
a = list(map(int, input().split()))

# 区間更新であるが、クエリごとにその変化を答えるためimos法はNG
# 不便さの更新に関係するのは、更新区間の左端と右端だけである
# そこで、各隣接区間の左-右(符号あり)と「不便さ」(左-右の絶対値の和)を計算しておき
# 左端と右端のそれぞれ変動しない方の隣接する場所との差の変化を求めて記録していく
# つまり、配列としては不便さ成分iを符号付きの標高差として持ちながら、
# 不便さの変化を計算するときだけ、前後の値をそれぞれ絶対値にすればよい

# 以下、符号の向きは左-右>0を正として固定する
unc = [] # 符号付き標高差を管理する配列
ans = 0 # 不便さの初期値
for i in range(n-1):
    x = a[i]-a[i+1]
    unc.append(x) 
    ans += abs(x)

for _ in range(q):
    l, r, v = map(int, sys.stdin.readline().split())
    # 0-indexedにあわせる
    l -= 1
    r -= 1

    if l==0:
        # クエリの左端が全区間の左端のときは、そこで不便さの更新は起きない
        pass
    else:
        x_bef = unc[l-1]
        x_aft = unc[l-1]-v
        # 符号付き標高差の更新
        # v>0、すなわち右が高くなるとき、標高差は小さくなる
        unc[l-1] -= v

        # 不便さを計算するときだけ、標高差の絶対値をとる
        unc_diff = abs(x_aft) - abs(x_bef)
        ans += unc_diff

    if r==n-1:
        # クエリの右端が全区間の右端のときは、そこで不便さの更新は起きない
        pass
    else:
        x_bef = unc[r]
        x_aft = unc[r]+v
        # v>0、すなわち左が高くなるとき、標高差は大きくなる
        unc[r] += v # 符号付き標高差の更新

        # 不便さを計算するときだけ、標高差の絶対値をとる
        unc_diff = abs(x_aft) - abs(x_bef)
        ans += unc_diff       

    print(ans)