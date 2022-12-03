a, b, c = map(int, input().split())

# 小数で比較すると誤差の影響が出るので、整数で扱えるなら整数で
# 両辺log2を除いて考えてOK

if a < c**b:
    print('Yes')
else:
    print('No')