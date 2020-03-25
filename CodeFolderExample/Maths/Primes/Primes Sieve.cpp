// 13
vector<int> sieve, primes;

// ~O(N * lg(lg(N)))
void primeSieve(int n) {
  sieve.assign(n + 1, 0);
  primes = {};
  for (int i = 3; i * i <= n; i += 2)
    if (!sieve[i])
      for (int j = i * i; j <= n; j += 2 * i)
        if (!sieve[j]) sieve[j] = i;
  primes.push_back(2);
  for (int i = 3; i < n; i++)
    if (!sieve[i] && (i & 1)) primes.push_back(i);
}