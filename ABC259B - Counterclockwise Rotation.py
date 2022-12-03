import math
a,b,d = map(int, input().split())
rad = math.radians(d)

# 原点周りにp0を回転
a1 = math.cos(rad)*a - math.sin(rad)*b
b1 = math.sin(rad)*a + math.cos(rad)*b

print(a1, b1)