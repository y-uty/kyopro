x, y, n = map(int, input().split())

if 3*x <= y:
    print(n*x)
else:
    tmp = n//3
    tmp2 = n%3
    ans = y*tmp
    ans += tmp2*x
    print(ans)