N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

# 数列A全体の累積和
import itertools
Acumsum = [0] + list(itertools.accumulate(A))

# rを1つずつ進めながら累積和の値に対する存在個数をdictに格納していく
# l~rの部分和はS_r - S_(l-1)
# 固定のrに対して、S_r - S_(l-1) = K を満たすような l の値の個数を求め、すべてのrでそれを繰り返せばよい
# -> 右端を固定して左端を動かしたとき、区間和がKとなるようなものがいくつあるか？
# それは、dictに格納された S_(l-1) = S_r - K の個数に等しい
from collections import defaultdict
cnt_cumsum = defaultdict(int)

for i in range(N):
    cnt_cumsum[Acumsum[i]] += 1
    ans += cnt_cumsum[Acumsum[i+1]-K]

print(Acumsum,cnt_cumsum, ans)
