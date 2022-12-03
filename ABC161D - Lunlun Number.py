import collections
k = int(input())

# ルンルン数を10**5個作る O(N)
# それを昇順に並び替える O(NlogN)
# K番目の数字を出力する O(1)
# => 全体で O(NlogN)

# ルンルン数はBFS的に作れる
anslist = [1,2,3,4,5,6,7,8,9]
lunlun = collections.deque(anslist)
cnt = 9
while cnt < 10**5:

    pre_num = lunlun.popleft()

    for i in range(10):
        if abs(pre_num%10 - i) <= 1:
            tmp = pre_num*10 + i
            lunlun.append(tmp)
            anslist.append(tmp)
            cnt += 1

print(sorted(anslist)[k-1])