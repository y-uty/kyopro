S = str(input())

if S[0] != 'A':
    print('WA')
    exit()

cnt = 0
sC = S[2:len(S)-1]
if len(sC) - len(sC.replace('C', '')) != 1:
    print('WA')
    exit()

sets = set(S[1] + S[2:].replace('C', ''))
atoz = set('abcdefghijklmnopqrstuvwxyz')
res = sets & atoz
if len(sets) == len(res):
    print('AC')
else:
    print('WA')