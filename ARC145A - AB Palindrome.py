n = int(input())
s = input()

if s in ('AB', 'BA'):
    print('No')
    exit()

# Aから始まるとき、Bで終わると、それはAに変えられない
# Bで終わるとき、Aで始まると、それはBに変えられない
# 先頭、末尾以外は、順番に変えていけば合わせることができる

if s[0]=='A' and s[-1]!='A':
    print('No')
elif s[-1]=='B' and s[0]!='B':
    print('No')
else:
    print('Yes')