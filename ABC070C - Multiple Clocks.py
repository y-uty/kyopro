n = int(input())
clocks = []

for _ in range(n):
    clocks.append(int(input()))

lcm_ = clocks[0]

import math
for i in range(n-1):
    lcm_ = (lcm_ * clocks[i+1]) // math.gcd(lcm_, clocks[i+1])

print(lcm_)