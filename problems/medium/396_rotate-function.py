class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        # F(0)
        f = sum(i * nums[i] for i in range(n))
        max_f = f
        # For k = 1 to n-1, compute F(k) from F(k-1)
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            if f > max_f:
                max_f = f
        return max_f