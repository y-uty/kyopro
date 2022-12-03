n = int(input())
s = [int(input()) for _ in range(n)]

s.sort()
s_sum = sum(s)
if s_sum%10 > 0:
    print(s_sum)
    exit()
else:
    for i in range(n):
        if s[i]%10 > 0:
            print(s_sum - s[i])
            exit()

print(0)