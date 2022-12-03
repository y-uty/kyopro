s = str(input())

# atcoder
t = []
for x in s:
    if x=='a': t.append(1)
    elif x=='t': t.append(2)
    elif x=='c': t.append(3)
    elif x=='o': t.append(4)
    elif x=='d': t.append(5)
    elif x=='e': t.append(6)
    else: t.append(7)

# print(t)

def bubble_sort(nlist):
    cnt = 0
    #配列の要素数num
    num = len(nlist)

    for i in range(num):
        swap = False
        for j in range(num-1, i, -1):
            #後ろから順番に隣同士の要素を比較する
            if nlist[j-1] > nlist[j]:
                nlist[j-1], nlist[j] = nlist[j], nlist[j-1]
                swap = True
                cnt += 1    
    
        #交換が行われなければ終了
        if swap == False:
            break
    
    return cnt

ans = bubble_sort(t)
print(ans)
