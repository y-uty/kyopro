s = input()
t = input()

offset = ord(t[0])-ord(s[0])
for i in range(len(s)):
    if t[i]==chr((ord(s[i])-97+offset)%26+97):
        continue
    else:
        print('No')
        exit()

print('Yes')