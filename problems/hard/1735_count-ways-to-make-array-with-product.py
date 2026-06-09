from typing import List

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        def get_prime_factors(num):
            factors = {}
            d = 2
            while d * d <= num:
                while num % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    num //= d
                d += 1
            if num > 1:
                factors[num] = factors.get(num, 0) + 1
            return factors
        
        # Precompute factorials and inverse factorials for combinations
        MAX_VAL = 10014  # n + e - 1 where n <= 10^4 and e <= 14
        fact = [1] * MAX_VAL
        for i in range(1, MAX_VAL):
            fact[i] = fact[i-1] * i % MOD
        
        # Compute modular inverse using Fermat's little theorem
        inv_fact = [1] * MAX_VAL
        inv_fact[MAX_VAL - 1] = pow(fact[MAX_VAL - 1], MOD - 2, MOD)
        for i in range(MAX_VAL - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        def comb(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD
        
        result = []
        for n, k in queries:
            if k == 1:
                result.append(1)
                continue
            
            factors = get_prime_factors(k)
            ways = 1
            
            for prime, exponent in factors.items():
                ways = (ways * comb(n + exponent - 1, exponent)) % MOD
            
            result.append(ways)
        
        return result