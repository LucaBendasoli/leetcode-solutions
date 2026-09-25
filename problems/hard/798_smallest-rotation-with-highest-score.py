from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)          # difference array, size n+1 for convenience

        for i, val in enumerate(nums):
            # Good interval when k <= i (i.e., k <= i) and k <= i - val
            if i >= val:
                diff[0] += 1
                diff[i - val + 1] -= 1

            # Good interval when k > i and k <= n + i - val
            if i + 1 < n:             # k can be at most n-1
                l = i + 1
                r = n + i - val
                if r > n - 1:
                    r = n - 1
                diff[l] += 1
                diff[r + 1] -= 1

        # Build prefix sum and find best k
        cur = 0
        best_k = 0
        best_score = -1
        for k in range(n):
            cur += diff[k]
            if cur > best_score:
                best_score = cur
                best_k = k

        return best_k