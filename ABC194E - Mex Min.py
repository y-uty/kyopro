n, m = map(int, input().split())
a = list(map(int, input().split()))

# AiはN(<=1500000)未満の非負整数ということに着目すると、
# Aiごとに登場するindexを調べて、その間隔がMを超えることがあるか、0から順に調べていける
# 見た目は二重ループだが、N個の要素を1個ずつpos(i, j)の二次元配列にマッピングしただけなので、
# 全体ではO(N)となる
# ただし、両端に注意

cnt = [[-1] for _ in range(n+1)]

for i in range(n):
    cnt[a[i]].append(i)

for i in range(n+1):
    if cnt[i][-1]==-1:
        print(i)
        exit()
    
    prev = -1
    for j in range(1, len(cnt[i])):
        if cnt[i][j] - prev > m:
            print(i)
            exit()
        
        prev = cnt[i][j]
    
    # 右端のケースをケア
    if n - prev > m:
        print(i)
        exit()
