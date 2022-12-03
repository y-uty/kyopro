import itertools
import collections
s1 = str(input())
s2 = str(input())
s3 = str(input())

cnt = collections.Counter(s1+s2+s3)
strnum = len(cnt.keys())
strtype = list(cnt.keys())
if strnum > 10:
    print('UNSOLVABLE')
    exit()

num = '0123456789'
permnum = itertools.permutations(num, strnum)

for p in permnum:
    if p[0]=='0': continue

    t1, t2, t3 = s1, s2, s3
    for i in range(strnum):
        t1 = t1.replace(strtype[i], p[i])
        if t1[0]=='0': break
        t2 = t2.replace(strtype[i], p[i])
        if t2[0]=='0': break
        t3 = t3.replace(strtype[i], p[i])
        if t3[0]=='0': break

    else:
        if int(t1)+int(t2)==int(t3):
            print(int(t1))
            print(int(t2))
            print(int(t3))
            exit()

print('UNSOLVABLE')