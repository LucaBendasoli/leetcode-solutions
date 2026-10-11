from __future__ import annotations

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if total <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans