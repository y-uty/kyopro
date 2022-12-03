import collections
k = int(input())
s = str(input())[:4]
t = str(input())[:4]

cards = [k]*10
for i in range(4):
    cards[int(s[i])] -= 1
    cards[int(t[i])] -= 1
    
rest_num = 9*k - 8

def calc_score(x, y):
    taka = 0
    aoki = 0
    s_cnt = collections.Counter(s + str(x))
    t_cnt = collections.Counter(t + str(y))
    for i in range(1, 10):
        taka += i * (10 ** s_cnt[str(i)])
        aoki += i * (10 ** t_cnt[str(i)])
    
    return taka, aoki

ans = 0
# 高橋君、青木君の残り1枚のカードが(i, j)であるときの両者のスコアを計算し、
# 高橋君の方がスコアが高い場合、その確率を計算し、それらの総和を取れば答え
for i in range(1, 10):
    for j in range(1, 10):
        taka, aoki = calc_score(i, j)

        if taka > aoki:
            prob_taka = cards[i] / rest_num
            cards[i] -= 1
            prob_aoki = cards[j] / (rest_num-1)
            # そのような選び方をするにはカードが足りないときはNG
            if prob_taka <= 0 or prob_aoki <= 0:
                pass
            else:
                ans += prob_taka*prob_aoki
            
            cards[i] += 1

print(ans)