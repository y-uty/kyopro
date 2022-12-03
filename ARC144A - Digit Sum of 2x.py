n = int(input())

d, m = divmod(n, 4)
x = '4'*d
if m > 0: x += str(m)
M = 0
for chr in x:
    M += int(chr)*2

print(M)
print(x[::-1])
