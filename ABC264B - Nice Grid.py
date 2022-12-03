r,c = map(int, input().split())

b = '#'
w = '.'
x = []
r1 = [b]*15
r2 = [b]+ [w]*13 + [b]
r3 = [b, w] + [b]*11 + [w, b]
r4 = [b, w, b] + [w]*9 + [b, w, b]
r5 = [b, w, b, w] + [b]*7 + [w,b,w,b]
r6 = [b, w, b, w, b] + [w]*5 + [b, w, b, w, b]
r7 = [b, w, b, w, b, w] + [b]*3 + [w, b, w, b, w, b]
r8 = [b, w, b, w, b, w, b] + [w] + [b, w, b, w, b, w, b]
r9 = [b, w, b, w, b, w] + [b]*3 + [w, b, w, b, w, b]
r10 = [b, w, b, w, b] + [w]*5 + [b, w, b, w, b]
r11 = [b, w, b, w] + [b]*7 + [w,b,w,b]
r12 = [b, w, b] + [w]*9 + [b, w, b]
r13 = [b, w] + [b]*11 + [w, b]
r14 = [b]+ [w]*13 + [b]
r15 = [b]*15

x.append(r1)
x.append(r2)
x.append(r3)
x.append(r4)
x.append(r5)
x.append(r6)
x.append(r7)
x.append(r8)
x.append(r9)
x.append(r10)
x.append(r11)
x.append(r12)
x.append(r13)
x.append(r14)
x.append(r15)

if x[r-1][c-1]=='#':
    print('black')
else:
    print('white')
    