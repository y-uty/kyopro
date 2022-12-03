import itertools
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

x, y, z = str(a[0]), str(a[1]), str(a[2])
xyz = [x, y, z]

perm = list(itertools.permutations(xyz))
ans = 0
for p in perm:
    tmp = int(p[0]+p[1]+p[2])
    ans = max(ans, tmp)

print(ans)