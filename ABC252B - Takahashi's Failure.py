n, k = map(int, input().split())
a = list(map(int, input().split()))
b = set(list(map(int, input().split())))

a_max = max(a)
a_set = set()
for i in range(n):
    if a[i]==a_max:
        a_set.add(i+1)

if len(a_set & b) > 0:
    print('Yes')
else:
    print('No')