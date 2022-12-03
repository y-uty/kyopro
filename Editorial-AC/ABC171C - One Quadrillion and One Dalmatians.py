n = int(input())
import collections
ans = collections.deque()
atoz = 'abcdefghijklmnopqrstuvwxyz'

while n > 0:
    # 26までは同じ桁なので1を引いて処理する
    m = (n-1) % 26
    ans.appendleft(atoz[m])
    n = (n-1) // 26

print(''.join(list(ans)))