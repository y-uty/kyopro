a, b, c = map(int, input().split())

if c % 2 == 0:
    if abs(a) > abs(b):
        print('>')
    elif abs(a) < abs(b):
        print('<')
    else:
        print('=')

else:
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')
