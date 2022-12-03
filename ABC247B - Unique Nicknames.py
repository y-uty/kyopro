n = int(input())
import collections
sd = collections.defaultdict(int)
td = collections.defaultdict(int)
sl = []
tl = []

for i in range(n):
    s, t = map(str, input().split())
    sl.append(s)
    tl.append(t)
    sd[s] += 1
    td[t] += 1

for i in range(n):
    scnt = sd[sl[i]]
    tcnt = td[sl[i]]

    if scnt + tcnt - (1 if sl[i]==tl[i] else 0)== 1:
        pass # OK

    else:
        scnt = sd[tl[i]]
        tcnt = td[tl[i]]
        
        if scnt + tcnt - (1 if sl[i]==tl[i] else 0) == 1:
            pass # OK

        else:          
            print('No')
            exit()
    
print('Yes')