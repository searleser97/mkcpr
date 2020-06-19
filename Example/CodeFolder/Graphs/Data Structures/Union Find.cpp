// 7
struct UnionFind {
  int n;
  vector<int> dad, size;

  UnionFind(int N) : n(N), dad(N), size(N, 1) {
    while (N--) dad[N] = N;
  }
  // 4
  // O(lg*(N))
  int root(int u) {
    if (dad[u] == u) return u;
    return dad[u] = root(dad[u]);
  }
  // 8
  // O(1)
  void join(int u, int v) {
    int Ru = root(u), Rv = root(v);
    if (Ru == Rv) return;
    if (size[Ru] > size[Rv]) swap(Ru, Rv);
    --n, dad[Ru] = Rv;
    size[Rv] += size[Ru];
  }
  // 4
  // O(lg*(N))
  bool areConnected(int u, int v) {
    return root(u) == root(v);
  }
  // 4
  int getSize(int u) { return size[root(u)]; }

  int numberOfSets() { return n; }
};