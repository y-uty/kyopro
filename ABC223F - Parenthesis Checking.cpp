#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
# define SORT(V) sort((V).begin(), (V).end())
# define RSORT(V) sort((V).rbegin(), (V).rend())
# define elif else if
# define rep(i,n) for (int i=0; i<n; i++)
// define for lazy segtree's constructor
using S = int;
using F = int;
S op(S a, S b) {return min(a, b);} // binary operation
F e() {return (int)(1e9+1);} // identity element
S mapping(F f, S x) {return x+f;}
F composition(F f, F g) {return f+g;}
F id() {return 0;} // identity mapping

int main() {
  int N, Q;
  string s;
  cin >> N >> Q >> s;
  
  vector<int> C(N);
  vector<string> P(N);
  if (s[0]=='(') C[0] = 1;
  else C[0] = -1;

  // '('を+1, ')'を-1に置き換え、その累積和をとった配列で区間クエリに答える
  // 左側'(' と 右側')' を入れ替えると、入れ替える前の左側の位置から、右側の位置の1つ手前までの累積和が -2 される
  // その逆では、 +2 される
  // 部分列でなく、文字列全体が正しい括弧列かを判定するには、「累積和が0に戻ること」「累積和が負にならないこと」となり、
  // これを任意の区間で考えると、「累積和が元に戻ること」「累積和が元の高さ未満にならないこと」となる

  for (int i=1; i<N; i++) {
    if (s[i]=='(') C[i] = C[i-1] + 1;
    else C[i] = C[i-1] - 1;
  }
  rep(i,N) {
    P[i] = s[i];
  }

  lazy_segtree<S, op, e, F, mapping, composition, id> segtr(C);

  int t, l, r;
  string ans;
  rep(i,Q) {
    cin >> t >> l >> r;
    l--; r--;
    string pl = P[l];
    string pr = P[r];

    if (t==1) { // 文字列の入れ替え
      if (pl==pr) continue; // 入れ替える括弧が同じ場合何もしなくてよい
      else {
        if (pl=="(") segtr.apply(l, r, -2);
        else segtr.apply(l, r, 2);
        swap(P[l], P[r]);
      }
    }
    else { // 正しい括弧列かの判定
    int vl = segtr.get(l); // クエリ区間の左端
    int vr = segtr.get(r); // クエリ区間の右端
    int vll; // 左端の1つ手前

    if (l==0) vll = 0;
    else vll = segtr.get(l-1);
      // 両端の高さが同じ and その区間の最小値が負にならない 場合に限り、Yes
      if (vll==vr and segtr.prod(l, r+1)-vll>=0) {
        ans = "Yes";
      }
      else ans = "No";
      cout << ans << endl;
    }
  }

}