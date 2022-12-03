import collections
n = int(input())
a = collections.deque(sorted(list(map(int, input().split()))))

# Ai = Ai mod Ajすると、Ai < Ajとなるので、
# 並び替えてあればdequeの出し入れで順番に操作できる
# 一回の操作でAiはAi/2以下になるので、愚直にシミュレーションしても間に合う
ans = 0
while len(a) > 1:
    mina = a.popleft()
    maxa = a.pop()

    maxmodmin = maxa%mina

    if maxmodmin==0:
        a.appendleft(mina)
    else:
        a.appendleft(mina)
        a.appendleft(maxmodmin)

    ans += 1
    
print(ans)