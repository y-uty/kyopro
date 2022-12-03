n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

min_trans = min([a,b,c,d,e])

if min_trans >= n:
    print(5)
else:
    import math
    print(math.ceil(n / min_trans)+4)