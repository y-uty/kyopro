s = str(input())

words = ['dream', 'dreamer', 'erase', 'eraser']
res = 'YES'

while len(s) > 0:
    for word in words:
        if s.startswith(word):
            s[len(word):] # 前方一致するぶんの文字数を削除
        else:
            res = 'NO'
            print(res)
            exit()
        break