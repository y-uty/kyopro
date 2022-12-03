N, M, Q = map(int, input().split())
abcds = []
for i in range(Q):
    abcds.append(list(map(int, input().split())))

ainit = [0 for _ in range(N)]
alist = []

# recursive function
def create_alist(arec, cnt=0, last=1):

    if cnt == N:
        alist.append(tuple(arec))
        return
    else:
        cnt += 1
        for i in range(last, M+1):
            arec[cnt-1] = i
            create_alist(arec, cnt, last)
            arec[cnt-1] = 0
            last += 1

create_alist(ainit) # create all A

# calculate points
dmax = 0
for a in alist:
    dsum = 0
    for q in abcds:
        if a[q[1]-1] - a[q[0]-1] == q[2]: # A_bi - A_ai = ci ?
            dsum += q[3]

    dmax = max([dmax, dsum])

print(dmax)