n,a,b = map(int, input().split())

ans = n*(n+1) // 2

x = n//a
px = a*(x*(x+1) // 2)

y = n//b
py = b*(y*(y+1) // 2)

import math
lcm_ = a*b // math.gcd(a, b)

xy = n//(lcm_)
pxy = (lcm_)*(xy*(xy+1) // 2)

print(ans-px-py+pxy)