// 10
typedef long long int li;

li binPow(li a, li p) {
  li ans = 1LL;
  while (p) {
    if (p & 1LL) ans *= a;
    a *= a, p >>= 1LL;
  }
  return ans;
}