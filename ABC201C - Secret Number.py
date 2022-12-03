S = input()
import collections
cnt = collections.defaultdict(list)
ans = 0

for i in range(len(S)):
    cnt[S[i]].append(i)

if (len(cnt['o']) > 4) or (len(cnt['x']) == 10):
    print(0)
    exit()

d = cnt['o'] + cnt['?']
import itertools
psecn = itertools.product(d, d, d, d)

for p in psecn:
    tf = True
    for i in cnt['o']:
        if i in set(p):
            tf = tf and True
        else:
            tf = tf and False
    
    if tf : ans += 1

print(ans)