N = int(input())

from collections import defaultdict
y_dict = defaultdict(list)

xy = []
for i in range(N):
    xy.append(list(map(int, input().split())))
    y_dict[xy[i][1]].append(i)

  
S = str(input())
for i in y_dict.keys():   
    llist = []
    rlist = []
    if len(y_dict[i]) >= 2:
        for k in y_dict[i]:
            if S[k] == 'L':
                llist.append(xy[k][0])
            else:
                rlist.append(xy[k][0])
            
        if len(llist) > 0 and len(rlist) > 0 and max(llist) > min(rlist):
                print('Yes')
                exit() 

print('No')