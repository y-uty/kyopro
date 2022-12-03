import math

a, b, n = map(int, input().split())

# a*x < b の場合、floorの中身が1未満なので、xの値によらず0にしかならない
# よって、そのようなx以下のnが与えられた場合、答えは0
if math.ceil(b/a) > n:
    print(0)
# 右項は、x>=b で 1以上、bより1小さいxを選べば良い
# ただし、そのようなxよりnが小さい場合は、nとする
else:
    if n >= b:
        x = b-1
        print(math.floor(a*x/b))
    else:
        print(math.floor(a*n/b))
