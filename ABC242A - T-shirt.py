a, b, c, x = map(int, input().split())

if x <= a:
    print(1)
elif x > b:
    print(0)
else:
    print(c / (b - a))
