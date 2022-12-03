import bisect
s = input()
t = input()
 
chrcnt = [[-1] for _ in range(26)]
for i in range(len(s)):
    chrcnt[ord(s[i])-97].append(i+1)

INF = 10**9
for i in range(26):
    chrcnt[i].append(INF)

cyc = 0
now = 0
for i in range(len(t)):
    x = ord(t[i])-97

    if len(chrcnt[x])==2:
        print(-1)
        exit()

    pos = bisect.bisect_right(chrcnt[x], now)
    now = chrcnt[x][pos]

    if now==INF:
        cyc += 1
        now = chrcnt[x][1]

print(cyc*len(s)+now)