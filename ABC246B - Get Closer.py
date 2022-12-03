a, b = map(int, input().split())

import math
d = math.sqrt(a**2 + b**2)

x = a / d
y = b / d

print(str(x) + ' ' +  str(y))