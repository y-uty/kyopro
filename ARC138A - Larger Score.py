import bisect
n, k = map(int, input().split())
a = list(map(int, input().split()))

# K+1項目以降で、はじめて自分より大きい数が出てくる場所がわかればよい
# これは、K+1項目からの累積Maxをつくることで、累積Maxのリストは広義単調増加となるため
# 二分探索でその場所を知ることができるようになる

# 「自分をK項目まで移動させる回数 + 初めて現れる自分より大きい数をK項目まで移動させる回数」
# を1~K項目までについてそれぞれ調べて、その最小値が答え
# ただし、二分探索の結果が累積Maxリストの右端だった場合、自分より大きい数が存在しない
# 従ってスコアをs+1以上にすることができないため、何もしない
# 1~K項目までですべて何もしなかった場合、スコアをs+1にすることは不可である

cmax = 0
cmax_list = []
for i in range(k, n):
    cmax = max(cmax, a[i])
    cmax_list.append(cmax)

ans = n
for i in range(k):
    idx = bisect.bisect_right(cmax_list, a[i])
    tmp = k-i + idx
    if idx==n-k: continue
    ans = min(ans, tmp)

if ans==n:
    print(-1)
else:
    print(ans)