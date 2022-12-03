def main():
    n = int(input())
    tr = defaultdict(list)
    edges = [-1]*(n-1)
    for i in range(n-1):
        a, b = map(int, stdin.readline().split())
        tr[a].append((b, i))
        tr[b].append((a, i))
    
    st = [1, -1]
    vx = deque([st])
    seen = [False]*(n+1)
    while vx:
        v_from, color_adj = vx.popleft()
        seen[v_from] = True

        color_num = 1

        for ve_to in tr[v_from]:
            v_to, e_num = ve_to
            if seen[v_to]: continue

            if color_adj==color_num: color_num += 1
            edges[e_num] = color_num
            vx.append([v_to, color_num])
            color_num += 1

    print(max(edges))
    print(*edges, sep='\n')


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

class Node:
    """ノード
    Attributes:
        key (any): ノードのキー。比較可能なものであれば良い。(1, 4)などタプルも可。
        val (any): ノードの値。
        lch (Node): 左の子ノード。
        rch (Node): 右の子ノード。
        bias (int): 平衡度。(左部分木の高さ)-(右部分木の高さ)。
        size (int): 自分を根とする部分木の大きさ

    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.lch = None
        self.rch = None
        self.bias = 0
        self.size = 1

class AVLTree:

    """https://qiita.com/tomato1997/items/2f9b3ac919d230ac68ec
    非再帰AVL木

    Attributes:
        root (Node): 根ノード。初期値はNone。
        default (any): ノード値のデフォルト値。デフォルトではNone。（数値、リストなど可）

    """

    def __init__(self, default=None):
        self.root = None
        self.default = default

    def rotate_left(self, v):
        u = v.rch
        u.size = v.size
        v.size -= u.rch.size + 1 if u.rch is not None else 1
        v.rch = u.lch
        u.lch = v
        if u.bias == -1:
            u.bias = v.bias = 0
        else:
            u.bias = 1
            v.bias = -1
        return u

    def rotate_right(self, v):
        u = v.lch
        u.size = v.size
        v.size -= u.lch.size + 1 if u.lch is not None else 1
        v.lch = u.rch
        u.rch = v
        if u.bias == 1:
            u.bias = v.bias = 0
        else:
            u.bias = -1
            v.bias = 1
        return u

    def rotateLR(self, v):
        u = v.lch
        t = u.rch
        t.size = v.size
        v.size -= u.size - (t.rch.size if t.rch is not None else 0)
        u.size -= t.rch.size + 1 if t.rch is not None else 1
        u.rch = t.lch
        t.lch = u
        v.lch = t.rch
        t.rch = v
        self.update_bias_double(t)
        return t

    def rotateRL(self, v):
        u = v.rch
        t = u.lch
        t.size = v.size
        v.size -= u.size - (t.lch.size if t.lch is not None else 0)
        u.size -= t.lch.size + 1 if t.lch is not None else 1
        u.lch = t.rch
        t.rch = u
        v.rch = t.lch
        t.lch = v
        self.update_bias_double(t)
        return t

    def update_bias_double(self, v):
        if v.bias == 1:
            v.rch.bias = -1
            v.lch.bias = 0
        elif v.bias == -1:
            v.rch.bias = 0
            v.lch.bias = 1
        else:
            v.rch.bias = 0
            v.lch.bias = 0
        v.bias = 0

    def insert(self, key, val=None):
        """挿入

        指定したkeyを挿入する。valはkeyのノード値。

        Args:
            key (any): キー。
            val (any): 値。（指定しない場合はvaldefaultが入る）

        Note:
            同じキーがあった場合は上書きする。

        """
        if val is None:
            val = copy.deepcopy(self.default)
        if self.root is None:
            self.root = Node(key, val)
            return

        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lch
            elif v.key < key:
                history.append((v, -1))
                v = v.rch
            elif v.key == key:
                v.val = val
                return

        p, pdir = history[-1]
        if pdir == 1:
            p.lch = Node(key, val)
        else:
            p.rch = Node(key, val)

        while history:
            v, direction = history.pop()
            v.bias += direction
            v.size += 1

            new_v = None
            b = v.bias
            if b == 0:
                break

            if b == 2:
                u = v.lch
                if u.bias == -1:
                    new_v = self.rotateLR(v)
                else:
                    new_v = self.rotate_right(v)
                break
            if b == -2:
                u = v.rch
                if u.bias == 1:
                    new_v = self.rotateRL(v)
                else:
                    new_v = self.rotate_left(v)
                break

        if new_v is not None:
            if len(history) == 0:
                self.root = new_v
                return
            p, pdir = history.pop()
            p.size += 1
            if pdir == 1:
                p.lch = new_v
            else:
                p.rch = new_v

        while history:
            p, pdir = history.pop()
            p.size += 1

    def delete(self, key):
        """削除

        指定したkeyの要素を削除する。

        Args:
            key (any): キー。

        Return:
            bool: 指定したキーが存在するならTrue、しないならFalse。

        """
        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lch
            elif v.key < key:
                history.append((v, -1))
                v = v.rch
            else:
                break
        else:
            return False

        if v.lch is not None:
            history.append((v, 1))
            lmax = v.lch
            while lmax.rch is not None:
                history.append((lmax, -1))
                lmax = lmax.rch

            v.key = lmax.key
            v.val = lmax.val

            v = lmax

        c = v.rch if v.lch is None else v.lch

        if history:
            p, pdir = history[-1]
            if pdir == 1:
                p.lch = c
            else:
                p.rch = c
        else:
            self.root = c
            return True

        while history:
            new_p = None

            p, pdir = history.pop()
            p.bias -= pdir
            p.size -= 1

            b = p.bias
            if b == 2:
                if p.lch.bias == -1:
                    new_p = self.rotateLR(p)
                else:
                    new_p = self.rotate_right(p)

            elif b == -2:
                if p.rch.bias == 1:
                    new_p = self.rotateRL(p)
                else:
                    new_p = self.rotate_left(p)

            elif b != 0:
                break

            if new_p is not None:
                if len(history) == 0:
                    self.root = new_p
                    return True
                gp, gpdir = history[-1]
                if gpdir == 1:
                    gp.lch = new_p
                else:
                    gp.rch = new_p
                if new_p.bias != 0:
                    break

        while history:
            p, pdir = history.pop()
            p.size -= 1

        return True

    def contains(self, key):
        """キーの存在チェック

        指定したkeyがあるかどうか判定する。

        Args:
            key (any): キー。

        Return:
            bool: 指定したキーが存在するならTrue、しないならFalse。

        """
        v = self.root
        while v is not None:
            if key < v.key:
                v = v.lch
            elif v.key < key:
                v = v.rch
            else:
                return True
        return False

    def get(self, key):
        """値の取り出し

        指定したkeyの値を返す。

        Args:
            key (any): キー。

        Return:
            any: 指定したキーが存在するならそのオブジェクト。存在しなければvaldefault

        """
        v = self.root
        while v is not None:
            if key < v.key:
                v = v.lch
            elif v.key < key:
                v = v.rch
            else:
                return v.val
        self.insert(key)
        return self[key]

    def lower_bound(self, key):
        """下限つき探索

        指定したkey以上で最小のキーを見つける。[key,inf)で最小

        Args:
            key (any): キーの下限。

        Return:
            any: 条件を満たすようなキー。そのようなキーが一つも存在しないならNone。

        """
        ret = None
        v = self.root
        while v is not None:
            if v.key >= key:
                if ret is None or ret > v.key:
                    ret = v.key
                v = v.lch
            else:
                v = v.rch
        return ret

    def upper_bound(self, key):
        """上限つき探索

        指定したkey未満で最大のキーを見つける。[-inf,key)で最大

        Args:
            key (any): キーの上限。

        Return:
            any: 条件を満たすようなキー。そのようなキーが一つも存在しないならNone。

        """
        ret = None
        v = self.root
        while v is not None:
            if v.key < key:
                if ret is None or ret < v.key:
                    ret = v.key
                v = v.rch
            else:
                v = v.lch
        return ret

    def find_kth_element(self, k):
        """小さい方からk番目の要素を見つける

        Args:
            k (int): 何番目の要素か(0オリジン)。

        Return:
            any: 小さい方からk番目のキーの値。
        """
        v = self.root
        s = 0
        while v is not None:
            t = s+v.lch.size if v.lch is not None else s
            if t == k:
                return v.key
            elif t < k:
                s = t+1
                v = v.rch
            else:
                v = v.lch
        return None

    def getmin(self):
        '''
        Return:
            any: 存在するキーの最小値
        '''
        if len(self) == 0:
            raise Exception('empty')
        ret = None
        v = self.root
        while True:
            ret = v
            v = v.lch
            if v is None:
                break
        return ret.key

    def getmax(self):
        '''
        Return:
            any: 存在するキーの最大値
        '''
        if len(self) == 0:
            raise Exception('empty')
        ret = None
        v = self.root
        while True:
            ret = v
            v = v.rch
            if v is None:
                break
        return ret.key

    def popmin(self):
        '''
        存在するキーの最小値をpopする
        Return:
            any: popした値
        '''
        if len(self) == 0:
            raise Exception('empty')
        ret = None
        v = self.root
        while True:
            ret = v
            v = v.lch
            if v is None:
                break
        del self[ret.key]
        return ret.key

    def popmax(self):
        '''
        存在するキーの最大値をpopする
        Return:
            any: popした値
        '''
        if len(self) == 0:
            raise Exception('empty')
        ret = None
        v = self.root
        while True:
            ret = v
            v = v.rch
            if v is None:
                break
        del self[ret.key]
        return ret.key

    def popkth(self, k):
        '''
        存在するキーの小さい方からk番目をpopする
        Return:
            any: popした値
        '''
        key = self.find_kth_element(k)
        del self[key]
        return key

    def get_key_val(self):
        '''
        Return:
            dict: 存在するキーとノード値をdictで出力
        '''
        retdict = dict()
        for i in range(len(self)):
            key = self.find_kth_element(i)
            val = self[key]
            retdict[key] = val
        return retdict

    def values(self):
        for i in range(len(self)):
            yield self[self.find_kth_element(i)]

    def keys(self):
        for i in range(len(self)):
            yield self.find_kth_element(i)

    def items(self):
        for i in range(len(self)):
            key = self.find_kth_element(i)
            yield key, self[key]

    def __iter__(self):
        return self.keys()

    def __contains__(self, key):
        return self.contains(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        return self.insert(key, val)

    def __delitem__(self, key):
        return self.delete(key)

    def __bool__(self):
        return self.root is not None

    def __len__(self):
        return self.root.size if self.root is not None else 0

    def __str__(self):
        return str(type(self)) + '(' + str(self.get_key_val()) + ')'

if __name__ == '__main__':
    from sys import stdin
    from math import sqrt, ceil, floor, factorial
    from collections import defaultdict, deque, Counter
    from heapq import heapify, heappop, heappush
    from itertools import accumulate, permutations, combinations, product
    import copy

    # int(input())
    # map(int, stdin.readline().split())
    # list(map(int, stdin.readline().split()))

    main()