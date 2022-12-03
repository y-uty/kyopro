n, k = map(int, input().split())

if k%10==0:
    print(1)
    exit()

anscand = [k]
strk = str(k)
revk = strk[::-1]

if k > int(revk):
    print(0)
    exit()

anscand.append(int(revk))

for _ in range(12):
    strk += '0'
    revk += '0'
    anscand.append(int(strk))
    anscand.append(int(revk))

cnt = 0
ansset = set(anscand)
for ans in ansset:
    if ans <= n:
        cnt += 1

# print(ansset)
print(cnt)