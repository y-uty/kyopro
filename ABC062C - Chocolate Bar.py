h, w = map(int, input().split())

anscand = []

# 縦に1回切る位置を固定して、残り1回は、縦or横で2等分する
for i in range(1, w): # 1~w-1
    s1 = h*i

    # 縦-縦に切る
    w_rest = w-i
    w_half2 = w_rest//2
    w_half3 = w_rest - w_half2

    s2 = h*w_half2
    s3 = h*w_half3

    tmp = max(s1, s2, s3) - min(s1, s2, s3)
    anscand.append(tmp)

    # 縦-横に切る
    h_half2 = h//2
    h_half3 = h-h_half2

    s2 = h_half2*w_rest
    s3 = h_half3*w_rest

    tmp = max(s1, s2, s3) - min(s1, s2, s3)
    anscand.append(tmp)

# 横に1回切る位置を固定して、残り1回は、縦or横で2等分する
for i in range(1, h): # 1~h-1
    s1 = w*i

    # 横-横に切る
    h_rest = h-i
    h_half2 = h_rest//2
    h_half3 = h_rest - h_half2

    s2 = w*h_half2
    s3 = w*h_half3

    tmp = max(s1, s2, s3) - min(s1, s2, s3)
    anscand.append(tmp)

    # 横-横に切る
    w_half2 = w//2
    w_half3 = w-w_half2

    s2 = w_half2*h_rest
    s3 = w_half3*h_rest

    tmp = max(s1, s2, s3) - min(s1, s2, s3)
    anscand.append(tmp)

print(min(anscand))