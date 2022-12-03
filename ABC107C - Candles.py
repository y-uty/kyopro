n, k = map(int, input().split())
x = list(map(int, input().split()))
ans = -1

x_neg = []
x_pos = [0]

if x[0] >= 0:
    print(x[k-1])
    exit()
if x[-1] <= 0:
    print(-1*x[-1*k])
    exit()  

candles = 0
for i in range(n):
    if x[i] < 0:
        x_neg.append(-1*x[i])
    elif x[i] > 0:
        x_pos.append(x[i])
    else:
        candles += 1

x_neg.append(0)
x_neg.sort()

# 負の方向に進む→どこかで正の方向に折り返す
i = 1 + candles
while True:
    if i + len(x_pos) - 1 >= k:

        dist = 2 * x_neg[i]
        dist += x_pos[k-i]

        if ans == -1 or dist < ans:
            ans = dist
        
        if i == k or i == len(x_neg)-1:
            break
    
    i += 1

# 正の方向に進む→   どこかで負の方向に折り返す
i = 1 + candles
while True:
    if i + len(x_neg) - 1 >= k: 

        dist = 2 * x_pos[i]
        dist += x_neg[k-i]

        if ans == -1 or dist < ans:
            ans = dist
        
        if i == k or i == len(x_pos)-1:
            break
    
    i += 1

print(ans)