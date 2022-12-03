N = int(input())
T, A = map(int, input().split())
H = [int(i) for i in input().split()]

difft = []

for h in H:
    avt_h = T - h * 0.006
    difft.append(abs(avt_h - A))

print(difft.index(min(difft))+1)