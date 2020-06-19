// 5
// cap[a][b] = Capacity left from a to b
// iflow = initial flow, icap = initial capacity
// pathMinCap = capacity bottleneck for a path (s->t)
// 4
typedef int T;
vector<int> level;
vector<vector<int>> adj, cap;
T inf = 1 << 30;
// 4
void init(int N) {
  adj.assign(N, vector<int>());
  cap.assign(N, vector<int>(N));
}
// 6
void addEdge(int u, int v, T icap, T iflow = 0) {
  if (!cap[u][v])
    adj[u].push_back(v), adj[v].push_back(u);
  cap[u][v] = icap - iflow;
  // cap[v][u] = cap[u][v]; // if graph is undirected
}
// 19
// O(N)
T bfs(int s, int t, vector<int> &dad) {
  dad.assign(adj.size(), -1);
  queue<pair<int, T>> q;
  dad[s] = s, q.push(s);
  while (q.size()) {
    int u = q.front().first;
    T pathMinCap = q.front().second;
    q.pop();
    for (int v : adj[u])
      if (dad[v] == -1 && cap[u][v]) {
        dad[v] = u;
        T flow = min(pathMinCap, cap[u][v]);
        if (v == t) return flow;
        q.push({v, flow});
      }
  }
  return 0;
}
// 14
// O(E^2 * V)
T maxFlowMinCut(int s, int t) {
  T maxFlow = 0;
  vector<int> dad;
  while (T flow = bfs(s, t, dad)) {
    maxFlow += flow;
    int u = t;
    while (u != s) {
      cap[dad[u]][u] -= flow, cap[u][dad[u]] += flow;
      u = dad[u];
    }
  }
  return maxFlow;
}