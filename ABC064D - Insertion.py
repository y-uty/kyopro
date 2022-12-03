import collections
n = int(input())
s = str(input())
ans = s

srep = ''
while s != srep:
    srep = s
    s = s.replace('()', '')
    if s=='':
        print(ans)
        exit()

scnt = collections.Counter(s)

ansl, ansr = '', ''
for _ in range(scnt[')']):
    ansl += '('

for _ in range(scnt['(']):
    ansr += ')'

print(ansl+ans+ansr)