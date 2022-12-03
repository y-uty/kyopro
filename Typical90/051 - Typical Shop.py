import collections
import bisect
n, k, p = map(int, input().split())
a = list(map(int, input().split()))

# K個(<=40)をL個とM個(<=20)にわけてbit全探索
l = n//2
m = n-l
al = a[:l]
am = a[l:]

# 選んだ個数ごとの合計金額記録表
l_choice = collections.defaultdict(list)
m_choice = collections.defaultdict(list)

# L個のbit全探索で記録表を埋めていく
for i in range(2**l):
    b = bin(i)[2:].zfill(l)

    price_sum = 0
    item_cnt = 0
    for j in range(l):
        if int(b[j]):
            price_sum += al[j]
            item_cnt += 1
    
    l_choice[item_cnt].append(price_sum)

# M個のbit全探索で記録表を埋めていく
for i in range(2**m):
    b = bin(i)[2:].zfill(m)

    price_sum = 0
    item_cnt = 0
    for j in range(m):
        if int(b[j]):
            price_sum += am[j]
            item_cnt += 1
    
    m_choice[item_cnt].append(price_sum)
    
# 記録表をソートする
for ke in l_choice.keys():
    l_choice[ke].sort()

for ke in m_choice.keys():
    m_choice[ke].sort()

# L+M=Kになるように、Lを固定して対応するMの記録表から
# 通り数を二分探索で見つける
ans = 0
for l_tmp in range(l+1):
    m_tmp = k-l_tmp
    for l_psum in l_choice[l_tmp]:
        if m_choice[m_tmp]:
            ans += bisect.bisect_right(m_choice[m_tmp], p-l_psum)

print(ans)