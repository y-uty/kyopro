a, b = map(int, input().split())

from decimal import Decimal, ROUND_HALF_UP
x = Decimal(str(b/a)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)

print(x)
