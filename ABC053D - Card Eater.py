import collections
n = int(input())
a = list(map(int, input().split()))

# 同じカードが奇数枚 -> 1枚にできる -> 1枚しかないとみなして良い
# 同じカードが偶数枚 -> 2枚残る
# 偶数枚をペアにする -> 1枚ずつにできる
# ペアにできず残った偶数枚 -> 1枚しかないものを1種類犠牲にして消す

# よって、答えは2枚以上あるカードのうち偶数枚となるカードの種類が
# 奇数 -> 元のカードの種類数
# 偶数 -> 元のカードの種類数 - 1

cnt = collections.defaultdict(int)
for i in range(n):
    cnt[a[i]] += 1

even_num = []
for k, v in cnt.items():
    if v%2==0:
        even_num.append(k)

if len(even_num)%2:
    print(len(cnt.keys())-1)
else:
    print(len(cnt.keys()))