import sys
import bisect
n = int(input())
a = list(map(int, input().split()))
q = int(input())

# Bi以上で最もBiに近いA, Bi以下で最もBiに近いAをそれぞれ探し、
# |Bi-Aj|, |Bi-Ak|のうち小さい方を選べば良い

# クエリ毎にAを全探索するとO(NQ)でTLEするため、探す部分は高速化したい
# Aを予め昇順に並べておいて、二分探索を使えばよい

# 二分探索で取得したindexはBi以上で最も近いAとなる
# Bi以下で最も近いAは、indexを1つ落とせば良い
# このとき、min(A)<=Bi, max(A)>=Biが気になるので、
# 両端に絶対選ばれないような値で番兵を入れておくとスッキリする
a.append(-10**9)
a.append(2*(10**9))
a.sort()

for _ in range(q):
    b = int(sys.stdin.readline())

    upper = bisect.bisect_left(a, b)
    lower = upper - 1

    if abs(a[upper]-b) > abs(a[lower]-b):
        print(abs(a[lower]-b))
    else:
        print(abs(a[upper]-b))
