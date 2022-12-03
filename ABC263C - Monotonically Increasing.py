import collections
n, m = map(int, input().split())

if n==1:
    for i in range(m):
        print(i+1)
    exit()

x = []
for i in range(m):
    x.append([i+1])

ans = []
x = collections.deque(x)

while x:
    t = x.popleft()

    mint = t[-1]
    for i in range(mint+1, m+1):
        t2 = t + [i]
        if len(t2)==n:
            ans.append(t2)
        else:
            x.append(t2)
    
ans.sort()
for i in range(len(ans)):
    print(*ans[i])