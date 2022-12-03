a, b, c = map(int, input().split())

expon_1tab = [
    [0,0,0,0],
    [1,1,1,1],
    [6,2,4,8],
    [1,3,9,7],
    [6,4,6,4],
    [5,5,5,5],
    [6,6,6,6],
    [1,7,9,3],
    [6,8,4,2],
    [1,9,1,9]
]

b_mod4 = b % 4
c_mod4 = c % 4
b_c_mod4 = expon_1tab[b_mod4][c_mod4]
a_1 = int(str(a)[-1])

print(expon_1tab[a_1][b_c_mod4%4])