n, x = map(int, input().split())

AtoZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = ''
for x in AtoZ:
    tmp = x*n
    ans += tmp

print(ans[x-1])