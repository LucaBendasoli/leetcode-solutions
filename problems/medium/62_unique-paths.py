class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Use a 1D DP array for space efficiency
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]