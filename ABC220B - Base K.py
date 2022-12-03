k = int(input())
a, b = map(int, input().split())

deci_a = 0
for i in range(len(str(a))):
    deci_a += (k ** i) * int(str(a)[len(str(a))-1-i])

deci_b = 0
for i in range(len(str(b))):
    deci_b += (k ** i) * int(str(b)[len(str(b))-1-i])

print(deci_a*deci_b)