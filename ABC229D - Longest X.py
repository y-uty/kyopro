s = str(input())
k = int(input())

len_s = len(s)

# 前提：連続するXの個数を可能な限り増やそうとするならば
# 　　　.の選び方はXを挟んで連続に取る必要がある

# .をXに変えられる場所のみ、そこまですべてXが連続した時のXの個数をリストに記録する
cnt_longest = [0]
for i in range(len_s):
    if s[i]=='.':
        cnt_longest.append(i+1)
cnt_longest.append(len_s+1)

# 作成したリストの任意の場所から右に向かってk個連続で.をXに置き換えた後、
# 始めて現れる.(k個先) - 直前の.(1個前) - 1 が、連続するXの個数となる(両開区間)
# この方法で計算するために、先に作成したリストの両端に0, |s|+1の要素を追加している

# .の個数が操作の上限回数なので、これがkより少ない場合はkを上書き
if len(cnt_longest)-2 < k: # 両端を除外した要素数
    k = len(cnt_longest)-2

ans = 0
for i in range(1, len(cnt_longest)-k+1-2+1): # len-2(両端)がベースとなる要素数、右開区間なので+1, 始点iを含めたk個を見るので-k+1
    tmp = cnt_longest[i+k] - cnt_longest[i-1] - 1
    if tmp > ans:
        ans = tmp

print(ans)