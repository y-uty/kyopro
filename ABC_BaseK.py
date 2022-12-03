# K進数の数をstrとして与え、10進数のintとして返す
def baseKto10(num_baseK, baseK):
    if type(num_baseK)==int:
        num_baseK = str(num_baseK)
    
    if num_baseK==0:
        return 0

    num_base10 = 0
    lennum = len(num_baseK)
    for i in range(lennum):
        num_base10 += int(num_baseK[-1-i]) * (baseK**i)
    
    return num_base10

# 10進数の数をintとして与え、K進数のstrとして返す
def base10toK(num_base10, baseK):
    if type(num_base10)==str:
        num_base10 = int(num_base10)

    if num_base10==0:
        return '0'

    num_baseK = []
    while num_base10 > 0:
        d = num_base10 // baseK
        m = num_base10 % baseK
        num_baseK.append(str(m))
        num_base10 = d
    
    return ''.join(num_baseK[::-1])