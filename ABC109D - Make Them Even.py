h, w = map(int, input().split())
masu = []
for _ in range(h):
    a = list(map(int, input().split()))
    masu.append(a)

# 左上から決めていく
# masu[i][j]=Even => 何もしない
# masu[i][j]=Odd => 右か下のうちOddの方に1枚移す, 両方Evenのとき, とりあえず右(いちばん右のときだけ下)へ
ans = []
for i in range(h):
    for j in range(w):

        if i==h-1 and j==w-1:
            break

        if masu[i][j]%2==1: # いまのマスが奇数のとき、コインを移す

            if i < h-1 and j < w-1: # 下にも右にもいける
                if masu[i+1][j]%2==1: # 下が奇数なら下へ
                    masu[i][j] -= 1
                    masu[i+1][j] += 1
                    ans.append((i+1, j+1, i+2, j+1))

                else: # それ以外、右が偶数でも右へ
                    masu[i][j] -= 1
                    masu[i][j+1] += 1
                    ans.append((i+1, j+1, i+1, j+2))

            elif j == w-1: # 右にはいけない
                masu[i][j] -= 1
                masu[i+1][j] += 1
                ans.append((i+1, j+1, i+2, j+1))

            else: # 下にはいけない
                masu[i][j] -= 1
                masu[i][j+1] += 1
                ans.append((i+1, j+1, i+1, j+2))

print(len(ans))
for x in ans:
    print(*x)

# for i in range(h):
#     print(*masu[i])