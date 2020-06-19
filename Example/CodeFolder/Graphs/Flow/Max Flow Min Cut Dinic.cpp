// 5
// cap[a][b] = Capacity from a to b
// flow[a][b] = flow occupied from a to b
// level[a] = level in graph of node a
// iflow = initial flow, icap = initial capacity
// pathMinCap = capacity bottleneck for a path (s->t)
// 5
typedef int T;
vector<int> level;
vector<vector<int>> adj;
vector<vector<T>> cap, flow;
T inf = 1 << 30;
// 5
void init(int N) {
  adj.assign(N, vector<int>());
  cap.assign(N, vector<int>(N));
  flow.assign(N, vector<int>(N));
}
// 7
void addEdge(int u, int v, T icap, T iflow = 0) {
  if (!cap[u][v])
    adj[u].push_back(v), adj[v].push_back(u);
  cap[u][v] += icap;
  // cap[v][u] = cap[u][v]; // if graph is undirected
  flow[u][v] += iflow, flow[v][u] -= iflow;
}
// 17
bool levelGraph(int s, int t) {
  level.assign(adj.size(), 0);
  level[s] = 1;
  queue<int> q;
  q.push(s);
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (int &v : adj[u]) {
      if (!level[v] && flow[u][v] < cap[u][v]) {
        q.push(v);
        level[v] = level[u] + 1;
      }
    }
  }
  return level[t];
}
// 14
T blockingFlow(int u, int t, T pathMinCap) {
  if (u == t) return pathMinCap;
  for (int v : adj[u]) {
    T capLeft = cap[u][v] - flow[u][v];
    if (level[v] == (level[u] + 1) && capLeft > 0)
      if (T pathMaxFlow = blockingFlow(
          v, t, min(pathMinCap, capLeft))) {
        flow[u][v] += pathMaxFlow;
        flow[v][u] -= pathMaxFlow;
        return pathMaxFlow;
      }
  }
  return 0;
}
// 9
// O(E * V^2)
T maxFlowMinCut(int s, int t) {
  if (s == t) return inf;
  T maxFlow = 0;
  while (levelGraph(s, t))
    while (T flow = blockingFlow(s, t, inf))
      maxFlow += flow;
  return maxFlow;
}