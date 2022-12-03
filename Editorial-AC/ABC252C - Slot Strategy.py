n = int(input())
reels = [str(input()) for _ in range(n)]

ans=10**9

import collections

# 0~9の場合を順番に調べて、その最小値がans
for i in range(10):
    num = collections.defaultdict(int)

    # i:0~9 がリールのどこに登場するかdictでカウント
    for j in range(n):
        idx = list(reels[j]).index(str(i))
        num[idx] += 1

    # 同じ場所に1回までの場合、その最大値
    # 複数回出る場合、場所をidxとするとidx*(回数-1)となる
    # 作ったdictのkeyが場所、valueが回数なので、このペアで計算した最大値がiに対する答え
    tmp = 0
    for k, v in num.items():
        tmp = max([tmp, k+10*(v-1)])
    
    if tmp < ans:
        ans = tmp

print(ans)