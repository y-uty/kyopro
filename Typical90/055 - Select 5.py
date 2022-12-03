n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

# 100C5 = 75,287,520 = 7.5*10^7
# PyPyなら単純な5重ループで間に合う
# ただし何も考えずに掛けていくととても大きな数になる可能性があるので、
# 1つ掛けるたびにあまりを取るほうがよい
# ちなみに、Pythonならitertools.combinations(list, 5)で簡単に書けるが
# 単純なforループよりは遅くなるのと、生成したイテレータはそのまま使わないとTLE

for i in range(n-4):
    for j in range(i+1, n-3):
        for k in range(j+1, n-2):
            for l in range(k+1, n-1):
                for m in range(l+1, n):
                    x = a[i]*a[j]
                    x %= p
                    x *= a[k]
                    x %= p
                    x *= a[l]
                    x %= p
                    x *= a[m]
                    if x%p==q: ans += 1
    
print(ans)