class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        # Place each number in its correct position if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        # Find the first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1