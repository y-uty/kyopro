abc = sorted(list(map(int, input().split())))
a, b, c = abc

ans = 0
# cをいくつ減らしたいか=cをbに合わせたい
x = c - b

# そのためには、そのぶんだけのaが必要
if x > a:
    print(-1)
    exit()
else:
    ans = x
    a -= x
    c -= x

# b,cがaになるまで2つの整数を1ずつ減らして
# a,b,cがそろったら3つ一気に減らす
# それは結局、b,cの数と同じ
ans += c
print(ans)