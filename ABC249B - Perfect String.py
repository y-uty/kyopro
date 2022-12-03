from tty import OFLAG


st = str(input())

atoz = set(list('abcdefghijklmnopqrstuvwxyz'))
AtoZ = set(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

oflg = False
kflg = False
stset = set()

for s in st:
    if s in atoz:
        kflg = True
    if s in AtoZ:
        oflg = True
    stset.add(s)

if kflg and oflg and len(st)==len(stset):
    print('Yes')
else:
    print('No')