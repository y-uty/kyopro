n = int(input())
a = [-1] + list(map(int, input().split()))
a_same = [False]*(n+1)

ans = 0

# i=aiを探す
cnt = 0
for i in range(1, n+1):
    if i==a[i]:
        a_same[i] = True
        cnt += 1

# i=aj, j=aiペアを探す
for i in range(1, n+1):
    if not a_same[i]:
        j = a[i]
        if j>i and a[j]==i:
            ans += 1

ans += cnt*(cnt-1)//2
print(ans)