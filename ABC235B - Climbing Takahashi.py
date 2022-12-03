N = input()
H = [int(i) for i in input().split()]
h_now = 0

for h in H:
    if h > h_now:
        h_now = h
    else:
        break

print(h_now)
