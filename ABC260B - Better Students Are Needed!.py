import collections
n,x,y,z = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
passed = [False]*(n+1)
ans = []

ax = []
bx = []
tt = []
for i in range(1, n+1):
    ax.append([a[i], -i])
    bx.append([b[i], -i])
    tt.append([a[i]+b[i], -i])

ax.sort(reverse=True)
bx.sort(reverse=True)
tt.sort(reverse=True)

for i in range(n):
    if x==0: break
    if passed[-ax[i][1]]==False:
        ans.append(-ax[i][1])
        x -= 1
        passed[-ax[i][1]] = True

for i in range(n):
    if y==0: break
    if passed[-bx[i][1]]==False:
        ans.append(-bx[i][1])
        y -= 1
        passed[-bx[i][1]] = True

for i in range(n):
    if z==0: break
    if passed[-tt[i][1]]==False:
        ans.append(-tt[i][1])
        z -= 1
        passed[-tt[i][1]] = True

print(*sorted(ans), sep='\n')