class sparse_table():
  def __init__(self, A, op):
    self.op = op
    self.tab = [A]
    self.N = len(A)
    self.K = self.N.bit_length()
    for i in range(1, self.K):
      l = 1 << i
      row = []
      for j in range(self.N-l+1):
        row.append( self.op(self.tab[i-1][j], self.tab[i-1][j+l//2]) )
      self.tab.append(row)
  
  def get(self, l, r): # given as [l, r]
    w = r-l+1
    k = w.bit_length()-1
    L = self.tab[k][l-1]
    R = self.tab[k][r-2**k]
    return self.op(L, R)