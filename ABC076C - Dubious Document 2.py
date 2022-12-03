s = list(str(input()))
slen = len(s)
t = list(str(input()))
tlen = len(t)

ngans = 'UNRESTORABLE'
anscand = []
if tlen > slen:
    print(ngans)
    exit()

for i in range(slen-tlen+1):
    # sのi文字目からtを比較.

    ngok = True
    for j in range(tlen):

        if s[i+j]==t[j] or s[i+j]=='?':
            continue
        else:
            ngok = False
            break

    if ngok:
        # 文字列候補に追加.
        anstmp = s[:i] + t + s[i+tlen:]
        anstmp = ''.join(anstmp).replace('?', 'a')
        anscand.append(anstmp)
        # 連続する「?」と、その前後で合致するtの部分の長さより、tの長さが小さい場合、合致するパターンが複数ある.
        # たとえば s:k???mi, t:su のようなケースでは、ksuami / kasumi(こっちが正解) が生成されうる.
        # そのため、前から合致するかを判定してksu?miで処理を打ち切るとNG.

if len(anscand)>0:
    # 候補の辞書順最小が答え.
    print(sorted(anscand)[0])
else:
    # 候補が無い場合'UNRESTORABLE'.
    print(ngans)