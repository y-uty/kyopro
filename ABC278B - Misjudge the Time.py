H, M = map(int, input().split())


timeset = []
idx_stt = -1
idx = 0
for i in range(24):
    for j in range(60):
        timeset.append((i, j))
        if (i, j)==(H, M):
            idx_stt = idx
        idx += 1

        # print(i, j)

while True:
    h, m = timeset[idx_stt%(24*60)]

    h = str(h).zfill(2)
    m = str(m).zfill(2)

    hh = h[0]+m[0]
    mm = h[1]+m[1]

    hh = int(hh)
    mm = int(mm)

    if (hh, mm) in timeset:
        print(int(h), int(m))
        exit()  

    idx_stt += 1