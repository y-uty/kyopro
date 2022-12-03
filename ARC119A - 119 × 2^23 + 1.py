N = int(input())

ans = []
b = 0
while 2**b <= N:
    a, c = divmod(N, 2**b)
    ans.append(a+b+c)
    b += 1

print(min(ans))