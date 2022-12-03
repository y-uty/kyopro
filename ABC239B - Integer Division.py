x = int(input())

from decimal import Decimal
import math

d = Decimal(x)
ans = math.floor(d)

print(ans)