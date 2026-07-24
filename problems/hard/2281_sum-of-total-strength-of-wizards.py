from typing import List

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)
        
        # Find previous and next smaller element for each index
        left = [-1] * n  # previous smaller or equal
        right = [n] * n  # next smaller (strictly)
        
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                right[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                left[stack.pop()] = i
            stack.append(i)
        
        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD
        
        # Prefix of prefix sums
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = (prefix_prefix[i] + prefix[i]) % MOD
        
        result = 0
        
        for i in range(n):
            l = left[i]  # previous smaller or equal
            r = right[i]  # next smaller (strictly)
            
            # For subarrays [left_idx, right_idx] where left_idx in (l, i] and right_idx in [i, r)
            # The sum contribution is:
            # sum over all such subarrays of sum(subarray)
            
            # Positive contribution: subarrays ending at positions [i, r-1]
            # Starting from positions (l, i]
            # Sum of (prefix[right_idx+1] - prefix[left_idx]) for left_idx in (l, i] and right_idx in [i, r-1]
            
            # For a fixed right_idx in [i, r-1]:
            # sum_{left_idx=l+1}^{i} (prefix[right_idx+1] - prefix[left_idx])
            # = (i - l) * prefix[right_idx+1] - sum_{left_idx=l+1}^{i} prefix[left_idx]
            # = (i - l) * prefix[right_idx+1] - (prefix_prefix[i+1] - prefix_prefix[l+1])
            
            # Sum over right_idx in [i, r-1]:
            # (i - l) * sum_{right_idx=i}^{r-1} prefix[right_idx+1] - (r - i) * (prefix_prefix[i+1] - prefix_prefix[l+1])
            
            positive = (i - l) * (prefix_prefix[r + 1] - prefix_prefix[i + 1]) % MOD
            negative = (r - i) * (prefix_prefix[i + 1] - prefix_prefix[l + 1]) % MOD
            
            total_sum = (positive - negative) % MOD
            contribution = (strength[i] * total_sum) % MOD
            result = (result + contribution) % MOD
        
        return result