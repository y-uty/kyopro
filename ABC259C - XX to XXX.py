s = str(input())
t = str(input())
slen = len(s)
tlen = len(t)

if tlen<slen:
    print('No')
    exit()

s += '#'
t += '#'

sc = []
stmp = s[0]
sa = [stmp, 1]
for i in range(1, slen+1):
    snow = s[i]
    if snow != stmp:
        sc.append(sa)
        sa = [snow, 1]
    else:
        sa[1] += 1
    stmp = snow

tc = []
ttmp = t[0]
ta = [ttmp, 1]
for i in range(1, tlen+1):
    tnow = t[i]
    if tnow != ttmp:
        tc.append(ta)
        ta = [tnow, 1]
    else:
        ta[1] += 1
    ttmp = tnow

if len(sc)!=len(tc):
    print('No')
    exit()

for i in range(len(sc)):
    if sc[i][0]==tc[i][0]: # 同じ文字であること
        if sc[i][1]==1: # sが連続1文字の場合、tも1文字でないと即NG
            if tc[i][1]==1:
                pass
            else:
                print('No')
                exit()

        else: # sが連続2文字以上の場合、sの連続数がt以下であれば挿入で一致可能
            if sc[i][1]<=tc[i][1]:
                pass
            else:
                print('No')
                exit()

    else: # 文字が異なれば即NG
        print('No')
        exit()

print('Yes')