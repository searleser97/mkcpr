// 3
// vis = visited
vector<vector<int>> adj;
vector<int> vis, toposorted;
// 4
void init(int N) {
  adj.assign(N, vector<int>());
  vis.assign(N, 0), toposorted.clear();
}

void addEdge(int u, int v) { adj[u].push_back(v); }
// 12
// returns false if there is a cycle
// O(E)
bool toposort(int u) {
  vis[u] = 1;
  for (auto &v : adj[u])
    if (v != u && vis[v] != 2 &&
        (vis[v] || !toposort(v)))
      return false;
  vis[u] = 2;
  toposorted.push_back(u);
  return true;
}
// 6
// O(V + E)
bool toposort() {
  for (int u = 0; u < adj.size(); u++)
    if (!vis[u] && !toposort(u)) return false;
  return true;
}