n = int(input())
a = list(map(int, input().split()))
p = 0

m = [0, 0, 0, 0]
for i in range(n):
    x = a[i]
    m[0] += 1
    for j in range(4):
        if 3-j+x > 3:
            p += m[-1-j]
        else:
            m[-1-j+x] += m[-1-j]

        m[-1-j] = 0

print(p)