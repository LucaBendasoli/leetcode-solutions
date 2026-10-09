class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = []
        third = -10**9 - 1  # smaller than any possible value

        for i in range(n - 1, -1, -1):
            if nums[i] < third:
                return True
            while stack and nums[i] > stack[-1]:
                third = max(third, stack.pop())
            stack.append(nums[i])

        return False