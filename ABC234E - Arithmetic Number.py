x = int(input())
xlen = len(str(x))

if xlen==1:
    print(x)
    exit()

# i: 1桁目がなにか 1-9
# j: 何個ずつ増やすかor減らすか 0-9 10以上になったらor0未満になったら作れないのでbreak
# k: 桁数 xの桁数-18桁(10**17のときは111111111111111111が答え)

anscand = []
ngflg = False
# 1桁目i
for i in range(1, 10):

    # 差分j
    for j in range(10):
        ans = str(i)
        utan = i

        # 増加
        for k in range(1, 19):
            utan += j
            if utan >= 10:
                break
            ans += str(utan)
            if int(ans) >= x:
                anscand.append(int(ans))

    # 差分j
    for j in range(10):
        ans = str(i)
        utan = i

        # 減少
        for k in range(1, 19):
            utan -= j
            if utan < 0:
                break
            ans += str(utan)
            if int(ans) >= x:
                anscand.append(int(ans))

print(min(anscand))
