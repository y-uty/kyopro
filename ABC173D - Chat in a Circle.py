import collections
n = int(input())
a = list(map(int, input().split()))
a.sort()
p = collections.deque(a)
c = collections.deque([p.pop()])
ans = 0

# Aiの人が割り込むと、Ai加算できる割り込みポイントが2つ増えることに注目
# これは、Aiの大きい順に割り込ませることで最大化できる
while p:
    p_now = p.pop()
    ans += c.popleft()
    c.append(p_now)
    c.append(p_now)

print(ans)
