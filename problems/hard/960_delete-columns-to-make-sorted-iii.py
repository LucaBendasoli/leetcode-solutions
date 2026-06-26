from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        if not strs or not strs[0]:
            return 0
        
        n = len(strs)
        m = len(strs[0])
        
        # dp[i] = max number of columns we can keep ending at column i
        dp = [1] * m
        
        for i in range(m):
            for j in range(i):
                # Check if column i can follow column j
                # (all rows must have strs[row][j] <= strs[row][i])
                can_follow = True
                for row in range(n):
                    if strs[row][j] > strs[row][i]:
                        can_follow = False
                        break
                
                if can_follow:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Maximum columns we can keep
        max_keep = max(dp)
        
        # Minimum columns to delete
        return m - max_keep