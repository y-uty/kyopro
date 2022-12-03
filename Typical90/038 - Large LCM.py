import math
a, b = map(int, input().split())

# LCM(a, b) = a *b / GCD(a, b)
# Pythonは整数のオーバーフロー気にしなくてOK
gcd_ = math.gcd(a, b)
lcm_ = a*b//gcd_

# if lcm_ > 10**18:
#     print('Large')
# else:
#     print(lcm_)


# オーバーフローを意識する(問題の趣旨をふまえる)解法
# a, bが大きくなりうるので、分離した式で判定できるようにする
# LCM(a, b) = a *b / GCD(a, b) > 10^18
# {10^18 / a} < {b / GCD(a, b)} で判定
if 10**18//a < b//gcd_:
    print('Large')
else:
    print(lcm_)