c11, c12, c13 = map(int, input().split())
c21, c22, c23 = map(int, input().split())
c31, c32, c33 = map(int, input().split())

if c11-c21==c12-c22 and c11-c21==c13-c23:

    if c21-c31==c22-c32 and c21-c31==c23-c33:

        print('Yes')
        exit()

print('No')