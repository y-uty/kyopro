def main():
    import sys
    h, w = map(int, input().split())
    masu = [0]*(h*w)
    uf = UnionFind(h*w)

    # 2次元H*Wのマスをリストにもち、0->1で赤く塗ることとする
    # 上下左右の移動で到達できるかの判定は、Union-Findの連結判定が使えれば高速
    # そこで、赤く塗った後に、そのマスの上下左右に赤マスがあるかを調べ、
    # ある場合はUnionすることで、「上下左右の移動で往来可能な連結成分」とすることができる

    q = int(input())
    for _ in range(q):
        qry = list(map(int, sys.stdin.readline().split()))

        # t==1: 赤く塗る+隣のマスが赤ければUnion
        if qry[0]==1:
            r, c = qry[1]-1, qry[2]-1
            idx = r*w+c
            masu[idx] = 1
            # 上下左右4マスのうち、赤に塗られているマスを調べる
            u, d, l, r = idx-w, idx+w, idx-1, idx+1
            # H*Wのマスからはみ出ないことを確認しながら、赤マスならUnionする
            if u>=0 and u<h*w:
                if masu[u]:
                    uf.union(u, idx)
            
            if d>=0 and d<h*w:
                if masu[d]:
                    uf.union(d, idx)

            if l//w==idx//w and l>=0 and l<h*w:
                if masu[l]:
                    uf.union(l, idx)

            if r//w==idx//w and r>=0 and r<h*w:
                if masu[r]:
                    uf.union(r, idx)

        # t==2: 2マスが互いに上下左右移動で到達できるか = Unionされているかの判定
        else:
            ra, ca, rb, cb = qry[1]-1, qry[2]-1, qry[3]-1, qry[4]-1
            idx_a = ra*w+ca
            idx_b = rb*w+cb

            # まず、2マスとも赤く塗られていることが必要
            if masu[idx_a] and masu[idx_b]:  

                # Union-Find木で同じrootなら、同一連結成分である     
                pt_a = uf.find(idx_a)
                pt_b = uf.find(idx_b)
                if pt_a==pt_b:
                    print('Yes')
                else:
                    print('No')

            else:
                print('No')


####################################################################################################
####################################################################################################

class UnionFind():
    def __init__(self, n):
        self.n = n
        # root: -1 * num of elements, others: their own parent.
        # To show, write print(uf.parents).
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # path compression; search for root, and connect to each parent.
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # If not yet; return 1(Done), already; return 0(Nothing).
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # union by rank;
        #  connect less-depth group to higher-depth one not to increase max-depth.
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return 1

    def size(self, x):
        return -self.parents[self.find(x)]

if __name__ == '__main__':
    main()