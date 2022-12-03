A, B, C, X, Y = map(int, input().split())
ans = 0

if (A + B) / 2 <= C:
    if X >= Y:
        ans += (A+B) * Y
        if A >= 2 * C:
            ans += C * 2 * (X - Y)
        else:
            ans += A * (X - Y)
    else:
        ans += (A+B) * X
        if B >= 2 * C:
            ans += C * 2 * (Y - X)
        else:
            ans += B * (Y - X)
    
    print(ans)
    exit()

if (A + B) / 2 > C:
    if X >= Y:
        ans += 2 * C * Y
        if A >= C*2:
            ans += C * 2 * (X - Y)
        else:
            ans += A * (X - Y)
    else:
        ans += 2 * C * X
        if B >= C*2:
            ans += C * 2 * (Y - X)
        else:
            ans += B * (Y - X)
    
    print(ans)
    exit()
