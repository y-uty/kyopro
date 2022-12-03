N, L, R = map(int, input().split())
A = list(map(int, input().split()))

# 最適な(x, y)の組を見つけたい
# x >= yは考える必要がない (∵ yを後から行うから、結局xはy-1になる)
# 最適なyがYだとしたとき、最適なx(<Y)が高速に求まれば間に合う(愚直だとO(N^2))
# これは、Yより左までの数列の和の最小値がわかればよい

# 見つけたいxより前では、Lに置き換えるより、Aのままのほうが総和が小さい = 直前までの和+A[i]
# 見つけたいxではそこまですべてLとするのが最小 = L*i
# 見つけたいxより後では、xまで全部Lはそのままで、以降はAを足していく = 直前までの和+A[i]
# よって、常に min(直前までの和+A[i], L*i) でYより左までの数列の和の最小値がO(1)で計算できる

# Yは最適と仮定しているから、Y以降の数列の和はL*(N-i)
# よって、このYに対する答えの候補は min(直前までの和, L*i) + L*(N-i) であり、
# これをすべてのYについて調べたうちの最小値が求める答えである

sum_left = 0
sum_right = R*N
anscand = [sum_left+sum_right]

for i in range(N):
    sum_left = min(sum_left+A[i], L*(i+1))
    sum_right = R*(N-(i+1))
    anscand.append(sum_left+sum_right)

print(min(anscand))