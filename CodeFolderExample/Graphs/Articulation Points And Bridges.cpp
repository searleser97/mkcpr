// 6
// APB = articulation points and bridges
// Ap = Articulation Point
// br = bridges, p = parent
// disc = discovery time
// low = lowTime, ch = children
// nup = number of edges from u to p
// 5
typedef pair<int, int> Edge;
int Time;
vector<vector<int>> adj;
vector<int> disc, low, isAp;
vector<Edge> br;

void init(int N) { adj.assign(N, vector<int>()); }
// 4
void addEdge(int u, int v) {
  adj[u].push_back(v);
  adj[v].push_back(u);
}
// 15
int dfsAPB(int u, int p) {
  int ch = 0, nup = 0;
  low[u] = disc[u] = ++Time;
  for (int &v : adj[u]) {
    if (v == p && !nup++) continue;
    if (!disc[v]) {
      ch++, dfsAPB(v, u);
      if (disc[u] <= low[v]) isAp[u]++;
      if (disc[u] < low[v]) br.push_back({u, v});
      low[u] = min(low[u], low[v]);
    } else
      low[u] = min(low[u], disc[v]);
  }
  return ch;
}
// 8
// O(N)
void APB() {
  br.clear();
  isAp = low = disc = vector<int>(adj.size());
  Time = 0;
  for (int u = 0; u < adj.size(); u++)
    if (!disc[u]) isAp[u] = dfsAPB(u, u) > 1;
}