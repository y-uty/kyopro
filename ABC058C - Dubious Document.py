n = int(input())
let_set = set(list('abcdefghijklmnopqrstuvwxyz'))

import collections
let_cnt = collections.defaultdict(int)

s = list(str(input()))
let_set &= set(s)
for x in s:
    let_cnt[x] += 1

for _ in range(n-1):
    s = list(str(input()))
    let_set &= set(s)
    s_cnt = collections.Counter(s)
    for k in s_cnt.keys():
        let_cnt[k] = min([s_cnt[k], let_cnt[k]])

ans = []
for k in let_cnt.keys():
    if k in let_set:
        ans += [k]*let_cnt[k]

print(''.join(sorted(ans)))