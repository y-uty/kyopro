import collections
n = int(input())
a = sorted(list(map(int, input().split())))

seen = collections.defaultdict(int)
amax = 10**9
for i in range(n):
    if seen[a[i]] > 0:
        a[i] = amax
        amax += 1
    else:
        seen[a[i]] += 1

a.sort()
a = collections.deque(a)

latest = 0
while a:
    minvol = a.popleft()

    if minvol==latest+1:
        latest += 1
    
    else:
        a.appendleft(minvol)

        maxvol1 = a.pop()
        if not a: break
        maxvlo2 = a.pop()
        latest += 1

print(latest)