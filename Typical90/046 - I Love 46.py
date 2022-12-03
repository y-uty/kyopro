import collections
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

amod46 = []
bmod46 = []
cmod46 = []
for i in range(n):
    amod46.append(a[i]%46)
for i in range(n):
    bmod46.append(b[i]%46)
for i in range(n):
    cmod46.append(c[i]%46)

acnt = collections.Counter(amod46)
bcnt = collections.Counter(bmod46)
ccnt = collections.Counter(cmod46)

ans = 0
for i in range(46):
    x = acnt[i]
    for j in range(46):
        y = bcnt[j]
        for k in range(46):
            z = ccnt[k]
        
            if (i+j+k)%46==0:
                ans += x*y*z

print(ans)