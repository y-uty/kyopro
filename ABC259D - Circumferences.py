def main():
    import sys
    n = int(input())
    sx,sy,tx,ty = map(int, input().split()) # s, tは必ずどれかの円周上の点
    circles = []
    circle_s, circle_t = -1, -1 # s,tがどの円の周上にいるか？
    for i in range(n):
        x,y,r = map(int, sys.stdin.readline().split())
        circles.append([x,y,r])
        if (sx-x)**2 + (sy-y)**2 == r**2: circle_s=i
        if (tx-x)**2 + (ty-y)**2 == r**2: circle_t=i

    uf = UnionFind(n)
    # 2円が交点を持つとき、Union-Findでつなげる
    for i in range(n-1):
        for j in range(1,n):
            # 中心間の距離が半径の差以下で、かつ半径の和以上か？
            cx1,cy1,r1 = circles[i]
            cx2,cy2,r2 = circles[j]
            dc = (cx1-cx2)**2 + (cy1-cy2)**2
            dr = (r1-r2)**2
            sr = (r1+r2)**2
            if dc >= dr and dc <= sr:
                res = uf.union(i, j) 

    # 点s,tのunion -> 既に連結ならOK、今回連結ならNG
    res = uf.union(circle_s, circle_t)
    if res: print('No')
    else: print('Yes')


class UnionFind():
    def __init__(self, n):
        self.n = n
        # root: -1 * num of elements, others: their own parent
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            # path compression; search for root, and connect to each parent
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # Unionでグループ数(=連結成分)が減少したかを確認するために、0 or 1をreturnするように改修
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 0

        # union by rank;
        #  connect less-depth group to higher-depth one not to increase max-depth
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return 1

    def size(self, x):
        return -self.parents[self.find(x)]

if __name__ == '__main__':
    main()