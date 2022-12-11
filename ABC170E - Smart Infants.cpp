#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
# define SORT(V) sort((V).begin(), (V).end())
# define RSORT(V) sort((V).rbegin(), (V).rend())
# define elif else if
# define rep(i,n) for (int i=0; i<n; i++)
// define for segtree's constructor
int op(int a, int b) {return min(a, b);} // binary operation
int e() {return (int)(1e9+1);} // identity element

int main() {
  int N, Q;
  cin >> N >> Q;

  // 幼児ごとのレート: vector
  vector<int> rate(N);
  // 幼児ごとの所属: vector
  vector<int> belong(N);
  // 幼稚園に所属する幼児がもつレートの一覧: vector<multiset>
  vector<multiset<int>> kinder(2e5);
  // 幼稚園ごとの最大のレートを保持してその最小値(平等さ)をもとめる: segtree
  segtree<int, op, e> fairness(2e5);

  int a, b;
  rep(i,N) { // 幼児のレート/所属, 幼稚園の所有レート
    cin >> a >> b; b--;
    rate[i] = a;
    belong[i] = b;
    kinder[b].insert(a);
  }

  rep(i,2e5) { // 幼稚園ごとの最大レート
    int cnt = kinder[i].size();
    if (cnt > 0) {
      auto max_kinder = *rbegin(kinder[i]);
      fairness.set(i, max_kinder);
    }
  }

  int c, d;
  rep(i,Q) { // クエリ処理
    cin >> c >> d; c--; d--;
    int rate_c = rate[c];
    int belong_before = belong[c];
    
    // 所属幼稚園の更新
    belong[c] = d;
    // 転園前後の幼稚園のレート情報の更新
    kinder[belong_before].erase(rate_c);
    kinder[d].insert(rate_c);
    // 転園前後の幼稚園の最大レートの更新
    // 転園元
    int cnt = kinder[belong_before].size();
    if (cnt==0) { // 幼稚園に幼児ゼロになる場合はinfに戻す
      fairness.set(belong_before, 1e9+1);
    }
    else {
      int max_kinder = *rbegin(kinder[belong_before]);
      fairness.set(belong_before, max_kinder);
    }
    // 転園先
    int max_kinder = *rbegin(kinder[d]);
    fairness.set(d, max_kinder);

    // 平等さの出力
    int ans = fairness.all_prod();
    cout << ans << endl;
  }


}
