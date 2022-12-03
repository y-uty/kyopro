s = str(input())
k = int(input())

ansset = set()
anslist = []

# K <= 5より、全ての部分文字列を考える必要はない
# 文字数ごとに、必ず1種類はユニークな部分文字列があるので、
# 辞書順K番目の部分文字列は、高々K文字である
# よって、K文字以下で作れる部分文字列のうち、辞書順K番目のものを出力すればOK
for l in range(1, k+1):
    for i in range(len(s)-l+1):
        substr = s[i:i+l]
        if substr not in ansset:
            anslist.append(substr)
            ansset.add(substr)

anslist.sort()
print(anslist[k-1])