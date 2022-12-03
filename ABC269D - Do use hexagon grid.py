def main():
    import sys
    n = int(input())

    # 2次元グリッドを塗ることを考える
    # 隣接する六角形を問題に指定されたとおりの6近傍ととらえればよい
    grid = [[-1]*2001 for _ in range(2001)]
    # 隣接判定と連結成分の個数カウントにはUnion-Findを使う
    uf = UnionFind(n)

    black = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        # 正の範囲に収まるように定数を加算 -> [0, 1000]となる
        x += 1000
        y += 1000
        grid[x][y] = i
        black.append([x, y])

    for i in range(n):
        x, y = black[i]

        if x-1>=0 and y-1>=0:
            if grid[x-1][y-1]>=0:
                uf.union(grid[x][y], grid[x-1][y-1])

        if x-1>=0:
            if grid[x-1][y]>=0:
                uf.union(grid[x][y], grid[x-1][y])

        if y-1>=0:
            if grid[x][y-1]>=0:
                uf.union(grid[x][y], grid[x][y-1])

        if y+1<=2000:
            if grid[x][y+1]>=0:
                uf.union(grid[x][y], grid[x][y+1])

        if x+1<=2000:
            if grid[x+1][y]>=0:
                uf.union(grid[x][y], grid[x+1][y])

        if x+1<=2000 and y+1<=2000:
            if grid[x+1][y+1]>=0:
                uf.union(grid[x][y], grid[x+1][y+1])

    ans = 0
    for i in range(n):
        # 根となる頂点の個数が、連結成分の個数
        if uf.parents[i] < 0: ans += 1
    print(ans)



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
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

if __name__=='__main__':
    main()
