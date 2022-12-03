import collections
s = list(str(input()))

scnt = collections.Counter(s)

for k, v in scnt.items():
    if v==1:
        print(k)
        exit()

print(-1)
