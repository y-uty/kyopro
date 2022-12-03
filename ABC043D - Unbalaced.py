s = str(input())
atoz = 'abcdefghijklmnopqrstuvwxyz'

# A, Bを任意の異なる文字としたとき、
# 'AA' or 'ABA' が存在すればその位置が答え
for tstr in atoz:
    cnt, l, r = 0, 0, 0
    for i in range(len(s)):
        if s[i]==tstr:
            if cnt==0:
                cnt += 1
                l = i
            else:
                cnt += 1
                r = i

                dif_ = r-l
                if dif_ == 1 or dif_ == 2:
                    ans = [l+1, r+1]
                    print(*ans)
                    exit()

                else:
                    l = i

print('-1 -1')