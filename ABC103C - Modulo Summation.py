n = int(input())
a = list(map(int, input().split()))
print(sum(a)-n)

### First AC submission ###
# n = int(input())
# a = list(map(int, input().split()))

# import math
# a_lcm = (a[0] * a[1]) // math.gcd(a[0], a[1])

# for i in range(2, n):
#     a_lcm = (a_lcm * a[i]) // math.gcd(a_lcm, a[i])

# ans = 0
# for i in range(n):
#     ans += (a_lcm - 1) % a[i]

# print(ans)