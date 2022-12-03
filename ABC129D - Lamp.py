import sys
h, w = map(int, input().split())
s = []
for _ in range(h):
    ss = list(str(sys.stdin.readline()))
    s.append(ss)

ans = 0
# s(i, j)が行方向に照らすことのできるマス数を求める
anslist = []
for i in range(h):
    lit = 0
    # 往路: 障害物に当たるまで左から連続何マス照らせるか
    for j in range(w):
        if s[i][j]=='#':
            lit = 0
        else:
            lit += 1 
        s[i][j] = lit     

    # 復路: 障害物に挟まれた区画ごとの最大値がその区画が照らせるマス数
    anstmp = 0
    ansrow = []
    for j in range(w-1, -1, -1):
        if s[i][j]==0:
            anstmp = 0
        else:
            anstmp = max([anstmp, s[i][j]])
        ansrow.append(anstmp)
    anslist.append(ansrow[::-1])

# s_T(i, j)が行方向に照らすことのできるマス数を求める
# すなわち、s(i, j)が列方向に照らすことのできるマス数を求める
anslist_t = []
for j in range(w):
    lit = 0
    # 往路: 障害物に当たるまで上から連続何マス照らせるか
    for i in range(h):
        if s[i][j]==0:
            lit = 0
        else:
            lit += 1       
        s[i][j] = lit

    # 復路: 障害物に挟まれた区画ごとの最大値がその区画が照らせるマス数
    # 求めると同時に、s(i, j)が照らせる全マス数を求めることが可能
    anstmp = 0
    ansrow = []
    for i in range(h-1, -1, -1):
        if s[i][j]==0:
            anstmp = 0
        else:
            anstmp = max([anstmp, s[i][j]])
    
            tmp = anstmp + anslist[i][j] - 1 # 自マス重複に注意
            if tmp > ans: ans = tmp

print(ans)