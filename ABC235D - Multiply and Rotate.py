import collections
a, n = map(int, input().split())

global xlist, cnt
xlist = collections.deque()
seen = set()
steps = collections.defaultdict(int)
steps[1] = 0
xlist.append(1)

while len(xlist) > 0:
    x = xlist.popleft()

    if len(str(a*x)) <= len(str(n)):
        if a*n in seen:
            pass
        else:
            xlist.append(a*x)
            seen.add(a*x)
            steps[a*x] = steps[x] + 1
        
    if x >= 10 and x % 10 > 0:
        rotated = int(str(x)[-1] + str(x)[:-1])
        if rotated in seen:
            pass
        else:
            xlist.append(rotated)
            seen.add(rotated)
            steps[rotated] = steps[x] + 1

if steps[n] == 0:
    print(-1)
else:
    print(steps[n])
