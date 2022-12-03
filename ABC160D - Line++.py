n, x, y = map(int, input().split())

import collections
ans = [0]*n

for i in range(1, n):
    for j in range(i+1, n+1):
        if i<=x:
            if j>=y:
                p = j-i - (y-x-1)
            else: # j<y
                p = min([x-i + 1 + y-j, j-i])

            ans[p] += 1

        elif i>x and i<y:
            if j<=y:
                p = min([i-x + y-j + 1, j-i])
            else: # j>y
                p = min([i-x + j-y + 1, j-i])
            
            ans[p] += 1
  
        else:
            p = j-i
            ans[p] += 1

        # print(i, j, p)

for i in range(1, n):
    print(ans[i])