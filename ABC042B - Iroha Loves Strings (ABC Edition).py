n, l = map(int, input().split())
slist = []
for _ in range(n):
    slist.append(str(input()))

slist.sort()

print(''.join(slist))
