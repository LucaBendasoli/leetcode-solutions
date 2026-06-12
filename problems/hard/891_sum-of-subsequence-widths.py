from typing import List

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        
        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD
        
        result = 0
        for i in range(n):
            # nums[i] as maximum: appears in 2^i subsequences
            # nums[i] as minimum: appears in 2^(n-1-i) subsequences
            contribution = (nums[i] * pow2[i] - nums[i] * pow2[n-1-i]) % MOD
            result = (result + contribution) % MOD
        
        return result