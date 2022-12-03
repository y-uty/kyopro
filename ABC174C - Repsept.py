import math
k = int(input())

ans = 1
mod_k = 7%k
mod_set = set()
# *10+7を繰り返すので、kで割ったあまりを*10+7して、それをkで割ったあまりが0になるかを繰り返せばよい
# 0になる前にあまりが重複したら、kの倍数にはならない
while True:
    if mod_k in mod_set:
        print(-1)
        exit()
    else:
        mod_set.add(mod_k)

    if mod_k==0:
        print(ans)
        exit()
    
    else:
        mod_k = (10*mod_k+7)%k
        ans += 1