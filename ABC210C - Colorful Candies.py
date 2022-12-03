N, K = map(int, input().split())

import collections
C = collections.deque(list(map(int, input().split())))
sel = collections.deque()
cnt = collections.defaultdict(int)
ans = 1

if N == K:
    print(len(set(C)))
    exit()

for i in range(K):
    c = C.popleft()
    sel.append(c)
    cnt[c] += 1
    
for i in range(N-K+1):
    if len(cnt) > ans:
        ans = len(cnt)
    if ans == K:
        print(ans)
        exit()

    if i == N-K:
        break

    c = C.popleft()
    cnt[c] += 1
    sel.append(c)
    c_del = sel.popleft()
    if cnt[c_del] == 1:
        cnt.pop(c_del)
    else:
        cnt[c_del] -= 1

print(ans)