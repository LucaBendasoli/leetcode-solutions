class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        dp = 1

        for num in nums:
            dp |= dp << num

        return ((dp >> target) & 1) == 1