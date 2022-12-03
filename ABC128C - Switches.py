n, m = map(int, input().split())

kslist = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    kslist.append(tmp)

p = list(map(int, input().split()))

ans = 0
for i in range(2**n):
    i2 = format(i, '0'+str(n)+'b')

    jdg =  True
    for j in range(m):
        if jdg:
            ks = kslist[j]
            k, slist = ks[0], ks[1:]

            oncnt = 0
            for s in slist:
                if i2[s-1]=='1':
                    oncnt += 1
            
            if oncnt%2==p[j]:
                pass
            else:
                jdg = False

    if jdg:    
        ans += 1

print(ans)