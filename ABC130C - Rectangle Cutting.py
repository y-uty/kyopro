w, h ,x, y = map(int, input().split())

if x*2==w and y*2==h:
    print(str(w*h/2) + ' 1')
else:
    print(str(w*h/2) + ' 0')