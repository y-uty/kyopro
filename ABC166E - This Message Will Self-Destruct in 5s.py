import collections
n = int(input())
a = list(map(int, input().split()))

# 絶対値を外し、iの式=jの式に整理する
# j > i とすれば、
# |j-i| = A[i]+A[j] => i+A[i] = j-A[j]
# よって、jを動かしつつ、過去のi+A[i]=現在のj-A[j]となる個数を数える
cnt = collections.defaultdict(int)
ans = 0
for i in range(n):
    ans += cnt[i-a[i]]
    cnt[i+a[i]] += 1

print(ans)


## 初回提出解法. AC後解説見てそちらがスマートなので ##
# b = []
# for i in range(n):
#     b.append(a[i]-(i-a[0]))

# for i in range(n):
#     cnt[b[i]] += 1

# ans = 0
# x = 0
# for i in range(n):
#     if i>0:
#         x -= 1+a[i]-a[i-1]
#     # print(x)
#     cnt[b[i]] -= 1
#     ans += cnt[x]

# print(ans)