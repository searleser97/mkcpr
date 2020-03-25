// 4
template <class T>
struct Matrix {
  int rows, cols;
  vector<vector<T>> m;
  // 3
  Matrix(int r, int c) : rows(r), cols(c) {
    m.assign(r, vector<T>(c));
  }
  // 2
  Matrix(const vector<vector<T>>& b)
      : rows(b.size()), cols(b[0].size()), m(b) {}
  // 4
  Matrix(int n) {
    m.assign(n, vector<T>(n));
    while (n--) m[n][n] = 1;
  }
  // 3
  vector<T>& operator[](int i) const {
    return const_cast<Matrix*>(this)->m[i];
  }
  // 8
  // O(N * M)
  Matrix operator+(const Matrix& b) {
    Matrix ans(rows, cols);
    for (int i = 0; i < rows; i++)
      for (int j = 0; j < m[i].size(); j++)
        ans[i][j] = m[i][j] + b[i][j];
    return ans;
  }
  // 8
  // O(N * M)
  Matrix operator-(const Matrix& b) {
    Matrix ans(rows, cols);
    for (int i = 0; i < rows; i++)
      for (int j = 0; j < m[i].size(); j++)
        ans[i][j] = m[i][j] - b[i][j];
    return ans;
  }
  // 10
  // O(N^3)
  Matrix operator*(const Matrix& b) {
    if (cols != b.rows) return Matrix(0, 0);
    Matrix ans(rows, b.cols);
    for (int i = 0; i < rows; i++)
      for (int j = 0; j < b[i].size(); j++)
        for (int k = 0; k < b.rows; k++)
          ans[i][j] += m[i][k] * b[k][j];
    return ans;
  }
  // 3
  Matrix& operator+=(const Matrix& b) {
    return *this = *this + b;
  }
  // 3
  Matrix& operator-=(const Matrix& b) {
    return *this = *this - b;
  }
  // 4
  Matrix& operator*=(const Matrix& b) {
    return *this = *this * b;
  }
};