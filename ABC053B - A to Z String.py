s = str(input())

# str型はイテラブル
Aidx = [i for i, Astr in enumerate(s) if Astr == 'A']
Zidx = [j for j, Zstr in enumerate(s) if Zstr == 'Z']

print(abs(min(Aidx)-max(Zidx))+1)