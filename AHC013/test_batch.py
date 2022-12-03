in_path_prefix = './in/'
in_path_suffix = '.txt'

out_path_prefix = './out/'
out_path_suffix = '.txt'

test_num = 100


x = '/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < '
for i in range(test_num):
    seqno = str(i).zfill(4)
    t = x + in_path_prefix + seqno + in_path_suffix
    print(t)




# for i in range(test_num):
#     seqno = str(i).zfill(4)
#     in_path = in_path_prefix + seqno + in_path_suffix
#     out_path = out_path_prefix + seqno + out_path_suffix
#     test003.main(in_path, out_path)

'''
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0000.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0001.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0002.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0003.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0004.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0005.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0006.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0007.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0008.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0009.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0010.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0011.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0012.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0013.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0014.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0015.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0016.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0017.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0018.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0019.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0020.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0021.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0022.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0023.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0024.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0025.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0026.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0027.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0028.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0029.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0030.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0031.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0032.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0033.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0034.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0035.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0036.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0037.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0038.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0039.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0040.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0041.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0042.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0043.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0044.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0045.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0046.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0047.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0048.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0049.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0050.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0051.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0052.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0053.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0054.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0055.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0056.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0057.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0058.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0059.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0060.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0061.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0062.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0063.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0064.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0065.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0066.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0067.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0068.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0069.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0070.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0071.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0072.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0073.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0074.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0075.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0076.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0077.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0078.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0079.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0080.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0081.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0082.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0083.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0084.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0085.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0086.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0087.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0088.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0089.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0090.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0091.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0092.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0093.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0094.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0095.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0096.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0097.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0098.txt
/usr/local/bin/python3 /Users/yuchiyama/Desktop/atcoder/AHC013/test003.py < ./in/0099.txt

'''
