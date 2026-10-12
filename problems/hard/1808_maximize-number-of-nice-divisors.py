class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        
        if primeFactors <= 3:
            return primeFactors
        
        if primeFactors % 3 == 0:
            return pow(3, primeFactors // 3, MOD)
        elif primeFactors % 3 == 1:
            return (pow(3, (primeFactors - 4) // 3, MOD) * 4) % MOD
        else:
            return (pow(3, (primeFactors - 2) // 3, MOD) * 2) % MOD