n = int(input())
a = [2]*(n+1)
a[1] = 1

# 篩の要領で、iの倍数たちの値を決めていく
# iと同じ値のときは+1する
# 同じ添字が別の倍数として観られるとき、同じ値のときに限って+1するイメージ
for i in range(2, n+1):
    x = a[i]
    j = i+i
    while j <= n:
        if a[j]==x:
            a[j] = x+1
        
        j = j+i

print(*a[1:])