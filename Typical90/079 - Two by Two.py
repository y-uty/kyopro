h, w = map(int, input().split())
a = []
for i in range(h):
    ar = list(map(int, input().split()))
    a.append(ar)
b = []
for i in range(h):
    br = list(map(int, input().split()))
    b.append(br)

# 操作によって各マスは+1/-1するだけで、
# その前後の操作や、自身以外のマスの状況から影響を受けないから、
# 操作の組み合わせを、どのような順序で行っても良い

# 従って、目標であるBに対して、Aの左上から操作を行う
# そうすると、必ず各行の右端、各列の下端以外はAとBをあわせることができる
# 逆に、各行の右端、各列の下端以を単独で調整することはできない
# よって、成否判定は(i, W)と(H, j)の箇所でA, Bの一致を確認すればよい

ans = 0
for i in range(h-1):
    for j in range(w-1):
        sa = b[i][j]-a[i][j]
        # B-Aが正なら加算、負なら減算が必要
        ans += abs(sa)
        # 2*2マスへの操作
        # (a[i][j]はもう参照しないので更新しなくてよい)
        a[i][j+1]+=sa
        a[i+1][j]+=sa
        a[i+1][j+1]+=sa

for i in range(h):
    if a[i][-1] != b[i][-1]:
        print('No')
        exit()
for i in range(w):
    if a[-1][i] != b[-1][i]:
        print('No')
        exit()

print('Yes')
print(ans)