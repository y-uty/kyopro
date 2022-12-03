import sys
q = int(input())

deck_above = []
deck_below = []

for _ in range(q):
    t, x = map(int, sys.stdin.readline().split())

    if t==1:
        deck_above.append(x)
    elif t==2:
        deck_below.append(x)
    else:
        if x <= len(deck_above):
            print(deck_above[-1-(x-1)])
        else:
            x -= len(deck_above)
            print(deck_below[x-1])