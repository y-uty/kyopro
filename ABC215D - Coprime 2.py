n, m = map(int, input().split())
a = list(map(int, input().split()))

a_divset = set()

# 1つの数に対する約数列挙 O(√N)
def make_divisors(n):
    divisors = set()
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n//i)
        i += 1
    return divisors

# Aiの新たな約数を集合に加える O(N)
for i in range(n):
    a_divset |= make_divisors(a[i])

# 1<=k<=Mに対してエラトステネスの篩の要領で
# 先に求めたAiの約数と共通しない整数のみを残す
ans_cnt = 1
not_ans = [False]*m
for i in range(2, m+1):
    if not_ans[i-1]:
        continue
    
    if i in a_divset:
        not_ans[i-1] = True
        for j in range(2*i, m+1, i):
            not_ans[j-1] = True
    else:
        ans_cnt += 1

# 篩の結果を用いて結果出力
print(ans_cnt)
for i in range(m):
    if not_ans[i]:
        pass
    else:
        print(i+1)