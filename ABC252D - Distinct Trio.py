n = int(input())
a = sorted(list(map(int, input().split())))

import collections
a_index = collections.defaultdict(int)
a_cnt = collections.Counter(a)

# 数ごとに初出のindexを格納
prev = a[0]
a_index[prev] = 0
for i in range(n):
    if prev != a[i]:
        a_index[a[i]] = i   
    prev = a[i]

ans = 0

numcnt = list(a_index.items())
for i in range(1, len(numcnt)-1): # 真ん中固定なので両端は除外
    num_center = numcnt[i][0]
    idx_center = numcnt[i][1]
    cnt_center = a_cnt[num_center]

    # 小さい方、大きい方から1つずつ選ぶ組み合わせ × 真ん中の数の個数
    # 個数は、冒頭で調べた「数ごとに初出のindex」で計算
    cnt_minor = idx_center
    cnt_major = n - numcnt[i+1][1]
    ans +=  cnt_center * cnt_minor * cnt_major

print(ans)