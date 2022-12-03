N = int(input())
ans = []

while N > 0:
    if N % 2 == 0:
        ans.append('B')
        N = N // 2
    else:
        ans.append('A')
        N -= 1

print(''.join(reversed(ans)))
