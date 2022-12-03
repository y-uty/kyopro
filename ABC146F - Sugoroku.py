n, m = map(int, input().split())
s = list(str(input()))[::-1]

i = 0
ans = []
while i < n:
    rest = n - i

    for j in range(min(m, rest), 0, -1):

        if s[i+j]=='0':
            i += j
            ans.append(j)
            break
    
    else:
        print(-1)
        exit()

print(*ans[::-1])
 