h1,h2,h3,w1,w2,w3 = map(int, input().split())

ans = 0
for xa in range(1, 29):

    for xb in range(1, 29):

        for xd in range(1, 29):

            for xe in range(1, 29):

                xc = h1-xa-xb
                if xc < 1: continue

                xf = h2-xd-xe
                if xf < 1: continue

                xg = w1-xa-xd
                if xg < 1: continue

                xh = w2-xb-xe
                if xh < 1: continue

                xi = w3-xc-xf
                if xi < 1: continue

                if xg+xh+xi != h3: continue

                ans += 1

print(ans)
