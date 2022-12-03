N = int(input())
A = list(map(int, input().split()))

Lv = [0]*(2*N+1 + 1) # アメーバ1~2N+1がどのレベル(=アメーバ1の何代子どもか)

for i in range(N):
    Parent = A[i]

    Lv[(i+1)*2] = Lv[Parent] + 1
    Lv[(i+1)*2+1] = Lv[Parent] + 1

print(*Lv[1:], sep='\n')
