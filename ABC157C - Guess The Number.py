n, m = map(int, input().split())

ans = '0'
for i in range(1, n):
    if i < n-1:
        ans = '0' + ans
    else:
        ans = '1' + ans

changed = [False]*n
for _ in range(m):
    s, c = map(int, input().split())
    if changed[s-1] and ans[s-1]!=str(c):
        print(-1)
        exit()
    else:
        ans = ans[:s-1] + str(c) + ans[s:]
        changed[s-1] = True

if len(ans)>1 and ans[0]=='0':
    print(-1)
else:
    print(ans)