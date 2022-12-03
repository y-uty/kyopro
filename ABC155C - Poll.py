import collections
sdict = collections.defaultdict(int)
anslist = []

n = int(input())
for i in range(n):
    s = str(input())
    sdict[s] += 1

vmax = max(sdict.values())
anslist = [k for k, v in sdict.items() if v == vmax]
anslist.sort()

for i in range(len(anslist)):
    print(anslist[i])