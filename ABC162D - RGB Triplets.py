n = int(input())
s = str(input())

cnt = [0, 0, 0]
rgb = []

def color_to_index(color):
    if color=='R':
        return 0
    elif color=='G':
        return 1
    else:
        return 2

for i in range(n):
    c = s[i]
    cnt[color_to_index(c)] += 1
    rgb.append(tuple(cnt))

ans = 0
for i in range(n-2):
    ci = s[i]
    for j in range(i+1, n-1):
        rgb_set = set(['R', 'G', 'B'])
        rgb_set.discard(ci)
        cj = s[j]
        rgb_set.discard(cj)

        if len(rgb_set)==1:
            ck = list(rgb_set)[-1]
            d = j-i
            not_k = j+d

            if not_k <= n-1 and s[not_k]==ck:
                except_ = 1
            else:
                except_ = 0

            ans += rgb[-1][color_to_index(ck)] - rgb[j][color_to_index(ck)] - except_
            
print(ans)