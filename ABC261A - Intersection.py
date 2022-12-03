a, b, c, d = map(int, input().split())

l = max([a,c])
r = min([b,d])

ans = max([r-l, 0])
print(ans)