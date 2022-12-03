N = int(input())
S = list(input()) + ['']

# Aの重みを2, Bの重みを1とすると、A<-->BBで重みの和は変わらない
# 単独のA, または隣接するBBのみが操作対象なので、Cは何もしない
# よって、AまたはBが連続している部分の重みの総和Wを求め、
# 偶数なら W//2個のAを、奇数なら W//2個のAと1個のBを順番に並べればよい

ans = []
w = 0
for i in range(N+1):
    s = S[i]

    if s=='A':
        w += 2
    elif s=='B':
        w += 1
    else:
        for _ in range(w//2):
            ans.append('A')
        for _ in range(w%2):
            ans.append('B')
        ans.append(s)
        w = 0

print(''.join(ans))