from __future__ import annotations

class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]
        ans = -10**9

        for i in range(m):
            for j in range(n):
                product = nums1[i] * nums2[j]
                dp[i][j] = product
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + product)
                ans = max(ans, dp[i][j])

        return ans