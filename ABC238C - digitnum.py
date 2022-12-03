n = int(input())

def dsum(a, l):
    k = l-a+1
    return (k*(k+1)) // 2

csum = 0
nlen = len(str(n))

for i in range(nlen):
    csum += dsum(10**i, min([n, (10**(i+1))-1]))

print(csum%998244353)
