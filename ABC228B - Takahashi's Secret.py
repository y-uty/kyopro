n, x = map(int, input().split())
a = list(map(int, input().split()))

i = 0
known = set([x])

while True:
    tmp = a[x-1]
    if tmp in known:
        print(len(known))
        exit()
    else:
        known.add(tmp)
        x = tmp