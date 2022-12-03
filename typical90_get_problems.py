import requests
from bs4 import BeautifulSoup
import pandas as pd
import collections

TARGET_URL = "https://atcoder.jp/contests/typical90/tasks"
html = requests.get(TARGET_URL) 
soup = BeautifulSoup(html.content, "html.parser")  
a_all = soup.select("a")

num = 1
a_all = collections.deque(a_all)
records = []
link_prefix = 'https://atcoder.jp'
while a_all:
    a = a_all.popleft()
    if len(a)>0 and a.contents[0] == format(num, '03'):
        a_link = a.attrs['href']
        a2 = a_all.popleft()        
        a_txt, a2_txt = a.contents[0], a2.contents[0]

        single_rec = [a_txt, a2_txt[:-4], a2_txt[-2], link_prefix+a_link]
        records.append(single_rec)
        num += 1

df_out = pd.DataFrame(records, columns=['No.', '問題名', '難易度', '問題リンク'])
df_out.to_csv('problems_list.csv', index=False)
## EOF ##