x,a,d,n = map(int, input().split())

if d==0:
    print(abs(a-x))
    exit()


tmp = abs((x-a))%abs(d)

an = a+d*(n-1)
if x >= max([a, an]):
    print(x-max([a, an]))
    exit()

if x <= min([a, an]):
    print(min([a, an])-x)
    exit()


if tmp <= abs(d)//2:
    print(tmp)
else:
    print(abs(d)-tmp)