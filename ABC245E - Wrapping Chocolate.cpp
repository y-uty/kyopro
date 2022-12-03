#include <bits/stdc++.h>
using namespace std;
# define SORT(V) sort((V).begin(), (V).end())
# define RSORT(V) sort((V).rbegin(), (V).rend())
# define elif else if
# define rep(i,n) for (int i=0; i<n; i++)

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A, B, C, D;
  rep(i,N) {int x; cin >> x; A.push_back(x);}
  rep(i,N) {int x; cin >> x; B.push_back(x);}
  rep(i,M) {int x; cin >> x; C.push_back(x);}
  rep(i,M) {int x; cin >> x; D.push_back(x);}

  // チョコと箱を縦の小さい順に並べて、箱が登場したら、入れられるチョコを入れていく
  // ただし、縦の同じチョコと箱がある場合、箱は後にしたい(その箱に同じ縦のチョコを入れられるかもしれない)
  // よって、縦, 種類(0:チョコ, 1:箱) でソートする
  vector<vector<int>> X;
  rep(i,N) {
    auto a = A[i];
    auto b = B[i];
    X.push_back({a, b, 0});
  }
  rep(i,M) {
    auto a = C[i];
    auto b = D[i];
    X.push_back({a, b, 1});
  }
  SORT(X);

  // 用意したチョコ/箱の配列を、順番に見ていく
  // チョコのとき、箱入れ待ちにする
  // 箱のとき、
  //   箱入れ待ちが空の場合、何もしない(後続のチョコは、その箱より必ず縦が長いので、もう役に立たない)
  //   そうでない場合、
  //     チョコの横が、箱の横以下で最大となるものを箱に入れるのが最適 -> 待ちチョコの管理に多重集合を用いて、処理としてはそのチョコを削除する
  //     そのようなものがない場合、その箱に入れられるチョコは存在しないので、何もしない
  auto K = N+M;
  multiset<int> choco;
  rep(i,K) {
    auto yoko = X[i][1];
    auto choco_box = X[i][2];

    // lower_bound(x)でx以上の最小 -> x以下で最大を見るためには、-xで集合を管理する
    if (choco_box==0) {
      choco.insert(-yoko);
    }
    else {
      auto itr = choco.lower_bound(-yoko);
      if (itr != choco.end()) {
        choco.erase(itr);
      }
    }
  }

  auto ans = choco.size();
  // 箱に入れられなかったチョコが1つでも残っていたらNo, そうでなければYes
  if (ans > 0) cout << "No" << endl;
  else cout << "Yes" << endl;

}