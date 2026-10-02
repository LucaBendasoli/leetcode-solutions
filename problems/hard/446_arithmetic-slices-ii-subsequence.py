from __future__ import annotations
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        dp = [{} for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_j = dp[j].get(diff, 0)
                count_i = dp[i].get(diff, 0)
                total += count_j
                dp[i][diff] = count_i + count_j + 1
                
        return total