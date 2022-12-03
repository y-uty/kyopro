#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
# define SORT(V) sort((V).begin(), (V).end())
# define RSORT(V) sort((V).rbegin(), (V).rend())
# define elif else if
# define rep(i,n) for (int i=0; i<n; i++)

int main() {
  int N, M;
  cin >> N >> M;

  // 有向グラフに閉路があればYes, なければNo
  // 強連結成分分解して、頂点数2以上の連結成分が存在すれば閉路あり

  // https://atcoder.github.io/ac-library/document_ja/scc.html
  scc_graph G(N);

  rep(i,M) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    G.add_edge(u, v);
  }
  
  auto SCC = G.scc();

  for (auto v : SCC) {
    auto vcnt = v.size();
    if (vcnt > 1) {
      cout << "Yes" << endl;
      return 0;
    }
  }
  
  cout << "No" << endl;

}