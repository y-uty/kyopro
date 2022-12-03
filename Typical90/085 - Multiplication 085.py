import math
k = int(input())

# abc=K<=10^12, a<=b<=cより、a, b, c <= 10^4
# a, bがわかればc=K/abで決まるため、a, bの組だけを全探索すればよい
# ざっくり10^8回で、実際はa<=bなのでもうちょっと少ないから大丈夫 

ans = 0
for a in range(1, min([10**4, k])+1):
    # abc=Kであるためには、Kがaで割り切れることが必要
    if k%a==0:
        bc = k//a
        for b in range(a, math.floor(math.sqrt(bc))+1):
            # bc(=K/a)がbで割り切れれば、abc=Kとなる(a,b,c)が存在するに十分
            if bc%b==0:
                ans += 1

print(ans)