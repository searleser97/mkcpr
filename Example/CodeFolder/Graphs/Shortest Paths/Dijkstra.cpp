// 6
// s = source
typedef int T;
typedef pair<T, int> DistNode;
T inf = 1 << 30;
vector<vector<int>> adj;
unordered_map<int, unordered_map<int, T>> weight;
// 4
void init(int N) {
  adj.assign(N, vector<int>());
  weight.clear();
}
// 7
void addEdge(int u, int v, T w, bool isDirected = 0) {
  adj[u].push_back(v);
  weight[u][v] = w;
  if (isDirected) return;
  adj[v].push_back(u);
  weight[v][u] = w;
}
// 16
// ~ O(E * lg(V))
vector<T> dijkstra(int s) {
  vector<long long int> dist(adj.size(), inf);
  priority_queue<DistNode> q;
  q.push({0, s}), dist[s] = 0;
  while (q.size()) {
    DistNode top = q.top();
    q.pop();
    int u = top.second;
    if (dist[u] < -top.first) continue;
    for (int &v : adj[u]) {
      T d = dist[u] + weight[u][v];
      if (d < dist[v]) q.push({-(dist[v] = d), v});
    }
  }
  return dist;
}