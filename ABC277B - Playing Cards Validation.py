N = int(input())

import collections
cards = collections.defaultdict(int)

for _ in range(N):
    S = input()

    if cards[S]:
        print('No')
        exit()
    cards[S] += 1

    s1, s2 = S[0], S[1]
    if s1 not in ('H', 'D', 'C', 'S'):
        print('No')
        exit()
    
    if s2 not in ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'):
        print('No')
        exit()


print('Yes')