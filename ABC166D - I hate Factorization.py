x = int(input())

for a in range(-1000, 1000+1):
    for b in range(-1000, 1000+1):
        if a**5 - b**5 == x:
            ans = [a, b]
            print(*ans)
            exit()