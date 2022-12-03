n = int(input())

b = [1]
for i in range(n):
    a = []
    if i==0:
        a.append(1)
        print(*a)
    else:
        for j in range(i+1):
            if j==0 or j==i:
                a.append(1)
            else:
                a.append(b[j-1]+b[j])

        print(*a)

    b = a