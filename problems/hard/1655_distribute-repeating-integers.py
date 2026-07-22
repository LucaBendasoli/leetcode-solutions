from typing import List
from collections import Counter

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        # Get frequencies of unique values
        freq = list(Counter(nums).values())
        m = len(quantity)
        n = len(freq)
        
        # Precompute sum of quantities for each subset of customers
        subset_sum = [0] * (1 << m)
        for mask in range(1 << m):
            total = 0
            for i in range(m):
                if mask & (1 << i):
                    total += quantity[i]
            subset_sum[mask] = total
        
        # dp[mask] = can we satisfy the customers in mask using frequencies seen so far
        dp = [False] * (1 << m)
        dp[0] = True  # Empty set is satisfied
        
        # For each unique frequency count
        for f in freq:
            # Process in reverse to avoid using same frequency multiple times
            new_dp = dp[:]
            for mask in range((1 << m) - 1, -1, -1):
                if not dp[mask]:
                    continue
                
                # Try all subsets of remaining customers
                remaining = ((1 << m) - 1) ^ mask
                submask = remaining
                
                # Iterate through all subsets of remaining
                while submask > 0:
                    # Check if this frequency can satisfy this subset
                    if subset_sum[submask] <= f:
                        new_dp[mask | submask] = True
                    submask = (submask - 1) & remaining
            
            dp = new_dp
        
        return dp[(1 << m) - 1]