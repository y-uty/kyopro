import collections
cards = collections.Counter(list(map(int, input().split())))

if len(cards) != 2:
    print('No')
else:
    for k, v in cards.items():
        if v == 2 or v == 3:
            pass
        else:
            print('No')
            exit()
        
    print('Yes')