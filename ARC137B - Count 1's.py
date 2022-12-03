n = int(input())
a = list(map(int, input().split()))
init_score = sum(a)

cmax = -10**9
cmax_list = []
cmin = 10**9
cmin_list = []
for i in range(n):
    x = 1 if a[i]==0 else -1
    cmax = max(cmax+x, x)
    cmax_list.append(cmax)

    cmin = min(cmin+x, x)
    cmin_list.append(cmin)


anslist = list(range(init_score+min(cmin_list), init_score+max(cmax_list)+1))
ansset = set(anslist)
ansset.add(init_score)
print(len(ansset))
