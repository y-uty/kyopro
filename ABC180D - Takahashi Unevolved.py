x, y, a, b = map(int, input().split())

cnt_a = 0
tmp = x
while True:
    tmp *= a
    # aを掛けることによる差分がb未満 かつ aを掛けた結果がy未満のとき、aを使う
    if x * (a ** (cnt_a+1)) - x * (a ** cnt_a) < b and x * (a ** cnt_a) < y:
        cnt_a += 1
    else:
        break
  
diff_ = y-1 - x * (a ** cnt_a)
cnt_b = diff_ // b
print(cnt_a + cnt_b)