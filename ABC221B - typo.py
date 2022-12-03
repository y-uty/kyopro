s = str(input())
t = str(input())

if s==t:
    print('Yes')
    exit()

for i in range(len(s)-1):
    comp = s[:i] + s[i+1] + s[i] + s[i+2:]
    if comp==t:
        print('Yes')
        exit()
        
print('No')