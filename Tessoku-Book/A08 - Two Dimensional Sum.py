h, w = map(int, input().split())
masu = []
for _ in range(h):
    x = list(map(int, input().split()))
    masu.append(x)

for i in range(h):
    for j in range(w-1):
        masu[i][j+1] += masu[i][j]

for j in range(w):
    for i in range(h-1):
        masu[i+1][j] += masu[i][j]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    # 左上(a, b)
    a -= 1
    b -= 1
    # 右下(c, d)
    c -= 1
    d -= 1

    ans = masu[c][d]
    if a > 0:
        ans -= masu[a-1][d] 
    if b > 0:
        ans -= masu[c][b-1]
    if a > 0 and b > 0:
        ans += masu[a-1][b-1]

    print(ans)
