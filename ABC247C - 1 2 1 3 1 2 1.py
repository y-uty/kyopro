n = int(input())

ans = ['1']
s = []

for i in range(2, n+1):
    ans = ans + [str(i)] + ans

print(' '.join(ans))
