n, k = map(int, input().split())
s = str(input())

# 辞書順最小は、先頭から貪欲に決める
# 先頭の文字a, bを比べると、b以降がどんなに小さくても、先頭aに勝てない
# よって、a, b, c,.., zの順にSを左から見て、最も左にあるものをTに加えて、
# 次は、加えた文字より右のSをまたa, b,..,zの順に見て、を繰り返せば良い
# しかし、(Tの文字数K)*(文字種M)*(元の文字列Sの長さ|S|)で最悪O(MK|S|)かかりTLEする

# そこで「Sのi文字目以降で、各文字が最も左にあるのは何文字目か？」を予め調べておくことで、
# 各文字ごとにSを左から見て、一番左の場所を見つける(存在するかを確かめる)処理をO(1)にできる
# 具体的には、「Sの残り文字列先頭index」としてS_headを持っていおいて、
# 答え文字列の長さK回のループの中で、文字種Mのループでa,b,..の順で
# 貪欲にS_head以降にその文字が存在するか、予め調べた情報からO(1)で判定し、
# あればTにその文字を追加してS_headをその文字が登場した位置に更新、
# なければ次の文字種へ、と処理していけばよい
# ただし各文字種の判定では、存在するかだけでなく「更新後のS_head以降全てを使ってK文字以上になること」
# もあわせて判定する必要がある(Noの場合、そもそもK文字作れなくなってしまうため)


# 前処理: prep_table[i][j]:= Sのi文字目以降で初めて文字列chr(j)が現れるSのindex の作成
# ord('a')が0となるようなオフセット
offset_ord = ord('a')
# prep_tableの初期化
prep_table = [[n]*26 for _ in range(len(s)+1)]
# prep_tableの作成; Sの後ろから見ていく
for i in range(len(s)-1, -1, -1):
    # 更新する文字種は1つだけなので、まずは1つ後ろと同じ値で全部埋める
    for x in range(26):
        prep_table[i][x] = prep_table[i+1][x]
    
    # Sのi文字目である文字種のみ、iで更新
    prep_table[i][ord(s[i])-offset_ord] = i


# 答えの文字列Tの作成
ans = ''
s_head = 0 # Sの残り文字列先頭index
for ans_i in range(k): # K文字ぶんのループ
    for j in range(26):
        s_i = prep_table[s_head][j]
        # K, |S|, 現在の|T| からその文字を選べるか判定
        if len(s) - s_i >= k - ans_i:
            ans += chr(j + offset_ord)
            s_head = s_i + 1
            break

print(ans)