#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
# define SORT(V) sort((V).begin(), (V).end())
# define RSORT(V) sort((V).rbegin(), (V).rend())
# define elif else if
# define rep(i,n) for (int i=0; i<n; i++)
// 区間Max取得・区間更新 lazy_segtree
using S = int; // 区間取得結果の型
using F = int; // 写像の型
// 二項演算
S op(S a, S b) {return max(a, b);}
// 単位元
S e() {return 0;}
// 恒等写像: 擬似的にlazy(=更新後の値)として取りえない値とする
const F ID = int(1e9);
F id() {return ID;}
// dataのノード値xに写像fを作用させる
S mapping(F f, S x) {
  if (f != ID) x = f; // fが恒等写像でないとき、xをfに書き換える
  return x;} // そうでないとき、xのまま
// lazyにたまっている写像gに、さらに写像fを作用させる(合成写像f∘g)
F composition(F f, F g) {
  if (f == ID) return g; // fが恒等写像のとき、gのまま(書き換えない)
  else return f;} // そうでないとき、fになる(より新しい方で書き換える)

int main() {
  int W, N;
  cin >> W >> N;

  vector<S> w(W+1);
  lazy_segtree<S, op, e, F, mapping, composition, id> segtr(w);

  int L, R, max_height, ans;
  rep(i,N) {
    cin >> L >> R;
    L--; R--;

    // 乗せる区間の、現在の高さの最大値+1が答え
    max_height = segtr.prod(L, R+1);
    ans = max_height+1;
    cout << ans << endl;

    // 出力した答えで、乗せた区間の高さを書き換える
    segtr.apply(L, R+1, ans);

  }

}