n, a, b = map(int, input().split())

for i in range(1, n*a+1):
    ans = ''
    for j in range(1, n*b+1):
        if ((j-1) // b) % 2 == 0:
            if ((i-1) // a) % 2 == 0:
                ans += '.'
            else:
                ans += '#'
        else:
            if ((i-1) // a) % 2 == 0:
                ans += '#'
            else:
                ans += '.'

    print(ans)