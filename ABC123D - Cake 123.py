import itertools
import heapq
x, y, z, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted(list(map(int, input().split())), reverse=True)

# 当然、ナイーブな全探索は不可能(10^9)
# AとBの組み合わせ(10^6)を決めた時、それに対してCを大きい順に選ぶ

# 優先度付きキューを使って、(A+B+C, Cの何番目に大きいものを選んだときか)を出し入れする
# A+B+Cの大きい順なので、Cだけを見るとまずはMax(C)を選ぶのがよいのは明らかなので
# そこからスタート

iters = itertools.product(a, b)
abc = []
for i in iters:
    ai, bi = i
    heapq.heappush(abc, (-1*(ai+bi+c[0]), 0)) # Maxをpopしたいので符号反転

for _ in range(min(k, x*y*z)):
    ans, c_idx = heapq.heappop(abc)
    ans *= -1
    print(ans)

    # そのA+Bに対して、次に大きいCを取る
    ans -= c[c_idx]
    c_idx += 1
    if c_idx < z:
        ans += c[c_idx]
        heapq.heappush(abc, (-1*ans, c_idx))
    # Cを選び切った場合、このA+Bの組み合わせは捨てる
