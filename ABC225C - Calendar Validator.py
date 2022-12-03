N, M = map(int, input().split())

import numpy as np
b_now = []
for i in range(N):
    B = list(map(int, input().split()))
    b_prev = b_now
    b_now = np.array(B)
    days = np.arange(b_now[0], b_now[0]+M)
    # 1ずつ単調増加である
    if np.all(b_now == days):
        q = -1
        # mod 7 が単調増加である（週をまたがない）
        for b in b_now:
            if ((b-1) % 7) < q:
                print('No')
                exit()
            q = ((b-1) % 7) - 1
        # 前配列と今回配列の各要素の差がいずれも7である（2週間以上先ではない）
        if i == 0: continue
        daydif = b_now - b_prev
        if np.all(daydif == 7):
            pass
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()

print('Yes')
