// 25
#include "../Number Theory/Modular Exponentiation.cpp"

bool isPrime(lli p, int k = 20) {
  if (p == 2 || p == 3) return 1;
  if ((~p & 1) || p == 1) return 0;
  lli d = p - 1, phi = d, r = 0;
  while (~d & 1) d >>= 1, r++;
  while (k--) {
    // set seed with: int main() { srand(time(0)); }
    lli a = 2 + rand() % (p - 3);  // [2, p - 2]
    lli e = pow(a, d, p), r2 = r;
    if (e == 1 || e == phi) continue;
    bool flag = 1;
    while (--r2) {
      e = multiply(e, e, p);
      if (e == 1) return 0;
      if (e == phi) {
        flag = 0;
        break;
      }
    }
    if (flag) return 0;
  }
  return 1;
}