n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

for i in range(n):
    cnt += abs(a[i]-b[i])

if cnt > k:
    print('No')
else:
    if (k-cnt)%2==0:
        print('Yes')
    else:
        print('No')
