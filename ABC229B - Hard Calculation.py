a, b = map(str, input().split())

for i in range(min(len(a), len(b))):
    if int(a[-1-i]) + int(b[-1-i]) >= 10:
        print('Hard')
        exit()

print('Easy')