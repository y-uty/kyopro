n = int(input())
a = list(map(int, input().split()))

if n==2:
    if sum(a)%2==0:
        print(sum(a))
    else:
        print(-1)
    
    exit()

a.sort(reverse=True)
ans = 0
for i in range(2):
    for j in range(i+1, n):
        tmp = a[i]+a[j]
        if tmp%2==0:
            ans = max(ans, tmp)

print(ans)