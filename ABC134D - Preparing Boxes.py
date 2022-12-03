n = int(input())
a = [-1] + list(map(int, input().split()))
balls = [0]*(n+1)

for i in range(n, 0, -1):
    j = i+i
    cnt = 0
    while j <= n:
        cnt += balls[j]
        j += i
    
    # aiとiの倍数の個数合計の偶奇が異なる場合のみ入れる
    if a[i]%2 ^ cnt%2:
        balls[i] += 1
    

if sum(balls)%2 == a[1]%2:
    print(sum(balls))
    anslist = []
    if sum(balls) > 0:
        for i in range(1, n+1):
            if balls[i] > 0:
                anslist.append(i)
        print(*anslist)
else:
    print(-1)
